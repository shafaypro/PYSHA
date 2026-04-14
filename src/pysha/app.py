"""Main assistant orchestrator.

Wires together:

- a configured :class:`STTEngine`, :class:`TTSEngine`, and :class:`LLMEngine`,
- discovered :class:`Skill` plugins,
- short-term + long-term :class:`ConversationMemory`,
- an :class:`EventBus` for observers (UI, logging, telemetry).

Intent routing is pragmatic: each skill publishes regex ``triggers`` for a
fast-path match.  If none match, the utterance goes straight to the LLM.
"""

from __future__ import annotations

import re
import uuid
from typing import Any

import structlog

from pysha.config import Settings
from pysha.core.engine import LLMEngine, STTEngine, TTSEngine
from pysha.core.events import Event, EventBus
from pysha.core.memory import ConversationMemory, MemoryStore
from pysha.core.plugin import PluginLoader
from pysha.skills.base import Skill, SkillContext

logger = structlog.get_logger(__name__)


class Assistant:
    """High-level façade that UIs (CLI, web, voice loop) talk to."""

    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.session_id = str(uuid.uuid4())

        self.events = EventBus()
        self.memory = ConversationMemory(system_prompt=settings.system_prompt())
        self.store = MemoryStore(settings.db_path)

        self.stt: STTEngine | None = None
        self.tts: TTSEngine | None = None
        self.llm: LLMEngine | None = None
        self.skills: dict[str, Skill] = {}

    # ------------------------------------------------------------------ lifecycle

    async def start(self) -> None:
        await self.store.open()
        self._load_engines()
        self._load_skills()
        if self.stt:
            await self.stt.start()
        if self.tts:
            await self.tts.start()
        if self.llm:
            await self.llm.start()
        await self.events.emit(Event("assistant.started", {"session_id": self.session_id}))
        logger.info(
            "assistant.ready",
            stt=self.stt.name if self.stt else None,
            tts=self.tts.name if self.tts else None,
            llm=self.llm.name if self.llm else None,
            skills=sorted(self.skills),
        )

    async def stop(self) -> None:
        for engine in (self.stt, self.tts, self.llm):
            if engine is not None:
                try:
                    await engine.stop()
                except Exception:
                    logger.warning("engine.stop_failed", exc_info=True)
        await self.store.close()
        await self.events.emit(Event("assistant.stopped"))

    # ------------------------------------------------------------------ plumbing

    def _load_engines(self) -> None:
        self.stt = self._load_engine("stt", self.settings.stt_engine, self._stt_kwargs())
        self.tts = self._load_engine("tts", self.settings.tts_engine, self._tts_kwargs())
        self.llm = self._load_engine("llm", self.settings.llm_engine, self._llm_kwargs())

    def _load_engine(self, kind: str, name: str, kwargs: dict[str, Any]) -> Any:
        try:
            return PluginLoader.load(f"pysha.engines.{kind}", name, **kwargs)
        except Exception as exc:
            logger.error("engine.load_failed", kind=kind, name=name, error=str(exc))
            return None

    def _stt_kwargs(self) -> dict[str, Any]:
        return {"language": self.settings.stt_language}

    def _tts_kwargs(self) -> dict[str, Any]:
        return {"voice": self.settings.tts_voice, "rate": self.settings.tts_rate}

    def _llm_kwargs(self) -> dict[str, Any]:
        name = self.settings.llm_engine
        if name == "anthropic":
            return {
                "api_key": self.settings.anthropic_api_key,
                "model": self.settings.anthropic_model,
            }
        if name == "openai":
            return {
                "api_key": self.settings.openai_api_key,
                "model": self.settings.openai_model,
            }
        if name == "ollama":
            return {
                "base_url": self.settings.ollama_base_url,
                "model": self.settings.ollama_model,
            }
        return {}

    def _load_skills(self) -> None:
        self.skills = PluginLoader.load_all("pysha.skills")

    # ------------------------------------------------------------------ public API

    async def handle_text(self, utterance: str) -> str:
        """Route *utterance* through the skill pipeline / LLM and return the reply."""
        utterance = utterance.strip()
        if not utterance:
            return ""
        self.memory.add("user", utterance)
        await self.store.save_message(self.session_id, "user", utterance)
        await self.events.emit(Event("user.message", {"text": utterance}))

        response = await self._route(utterance)

        self.memory.add("assistant", response)
        await self.store.save_message(self.session_id, "assistant", response)
        await self.events.emit(Event("assistant.message", {"text": response}))
        return response

    async def speak(self, text: str) -> None:
        if self.tts:
            await self.tts.speak(text)

    # ------------------------------------------------------------------ routing

    async def _route(self, utterance: str) -> str:
        skill = self._match_skill(utterance)
        if skill is not None:
            try:
                result = await skill.handle(
                    SkillContext(utterance=utterance, memory=self.memory, store=self.store)
                )
                if result.handled and result.response:
                    return result.response
            except Exception:
                logger.warning("skill.handle_failed", skill=skill.name, exc_info=True)
        return await self._ask_llm(utterance)

    def _match_skill(self, utterance: str) -> Skill | None:
        for skill in self.skills.values():
            for pattern in skill.triggers:
                if re.search(pattern, utterance, re.IGNORECASE):
                    logger.debug("skill.matched", skill=skill.name, pattern=pattern)
                    return skill
        return None

    async def _ask_llm(self, utterance: str) -> str:
        if self.llm is None:
            return "I don't have a language model configured."
        resp = await self.llm.chat(self.memory.to_llm_messages())
        return resp.content.strip()
