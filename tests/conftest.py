"""Shared test fixtures."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import AsyncIterator

import pytest

from pysha.app import Assistant
from pysha.config import Settings
from pysha.core.engine import LLMMessage, LLMResponse, Transcript


@pytest.fixture
def settings(tmp_path) -> Settings:
    return Settings(
        stt_engine="fake",
        tts_engine="fake",
        llm_engine="fake",
        anthropic_api_key="x",
        data_dir=tmp_path,
    )


# -------- fakes --------

@dataclass
class FakeLLM:
    name: str = "fake"
    last_messages: list[LLMMessage] = field(default_factory=list)
    canned_reply: str = "fake-reply"

    async def start(self) -> None: ...
    async def stop(self) -> None: ...

    async def chat(self, messages, *, temperature=0.7, max_tokens=1024):
        self.last_messages = messages
        return LLMResponse(content=self.canned_reply, model="fake")

    async def stream_chat(self, messages, *, temperature=0.7, max_tokens=1024):
        yield self.canned_reply


@dataclass
class FakeSTT:
    name: str = "fake"

    async def start(self) -> None: ...
    async def stop(self) -> None: ...

    async def transcribe(self, audio_bytes, *, language="en"):
        return Transcript(text="hello", language=language)

    async def stream(self, *, language="en") -> AsyncIterator[Transcript]:
        yield Transcript(text="hello", language=language)


@dataclass
class FakeTTS:
    name: str = "fake"
    spoken: list[str] = field(default_factory=list)

    async def start(self) -> None: ...
    async def stop(self) -> None: ...

    async def synthesize(self, text: str) -> bytes:
        return b""

    async def speak(self, text: str) -> None:
        self.spoken.append(text)


@pytest.fixture
async def assistant(settings) -> Assistant:
    asst = Assistant(settings)
    await asst.store.open()
    asst.stt = FakeSTT()
    asst.tts = FakeTTS()
    asst.llm = FakeLLM()
    asst._load_skills()
    yield asst
    await asst.store.close()
