"""Ollama local-LLM engine.

Runs fully on-device (llama3, mistral, phi-3, etc.).
Install with: ``pip install 'pysha[llm-ollama]'``
"""

from __future__ import annotations

from typing import AsyncIterator

import structlog

from pysha.core.engine import LLMMessage, LLMResponse

logger = structlog.get_logger(__name__)


class OllamaLLMEngine:
    name = "ollama"

    def __init__(
        self,
        model: str = "llama3.1",
        base_url: str = "http://localhost:11434",
        **_: object,
    ) -> None:
        self._model = model
        self._base_url = base_url
        self._client = None

    async def start(self) -> None:
        try:
            from ollama import AsyncClient  # type: ignore[import-not-found]
        except ImportError as exc:
            raise RuntimeError(
                "Install the LLM extra:  pip install 'pysha[llm-ollama]'"
            ) from exc
        self._client = AsyncClient(host=self._base_url)
        logger.info("llm.ollama.ready", model=self._model, host=self._base_url)

    async def stop(self) -> None:
        self._client = None

    async def chat(
        self,
        messages: list[LLMMessage],
        *,
        temperature: float = 0.7,
        max_tokens: int = 1024,
    ) -> LLMResponse:
        assert self._client is not None
        resp = await self._client.chat(
            model=self._model,
            messages=[{"role": m.role, "content": m.content} for m in messages],
            options={"temperature": temperature, "num_predict": max_tokens},
        )
        return LLMResponse(content=resp["message"]["content"], model=self._model)

    async def stream_chat(
        self,
        messages: list[LLMMessage],
        *,
        temperature: float = 0.7,
        max_tokens: int = 1024,
    ) -> AsyncIterator[str]:
        assert self._client is not None
        stream = await self._client.chat(
            model=self._model,
            messages=[{"role": m.role, "content": m.content} for m in messages],
            options={"temperature": temperature, "num_predict": max_tokens},
            stream=True,
        )
        async for part in stream:
            text = part.get("message", {}).get("content", "")
            if text:
                yield text
