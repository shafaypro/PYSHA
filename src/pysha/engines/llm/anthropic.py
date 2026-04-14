"""Anthropic Claude engine.

Install with: ``pip install 'pysha[llm-anthropic]'``
"""

from __future__ import annotations

from typing import AsyncIterator

import structlog

from pysha.core.engine import LLMMessage, LLMResponse

logger = structlog.get_logger(__name__)


class AnthropicLLMEngine:
    """Claude via the official Anthropic Python SDK."""

    name = "anthropic"

    def __init__(
        self,
        api_key: str | None = None,
        model: str = "claude-sonnet-4-20250514",
        **_: object,
    ) -> None:
        self._api_key = api_key
        self._model = model
        self._client = None

    async def start(self) -> None:
        try:
            from anthropic import AsyncAnthropic  # type: ignore[import-not-found]
        except ImportError as exc:
            raise RuntimeError(
                "Install the LLM extra:  pip install 'pysha[llm-anthropic]'"
            ) from exc
        self._client = AsyncAnthropic(api_key=self._api_key)
        logger.info("llm.anthropic.ready", model=self._model)

    async def stop(self) -> None:
        if self._client is not None:
            await self._client.close()
            self._client = None

    @staticmethod
    def _split(messages: list[LLMMessage]) -> tuple[str, list[dict]]:
        system_chunks = [m.content for m in messages if m.role == "system"]
        convo = [
            {"role": m.role, "content": m.content}
            for m in messages
            if m.role in {"user", "assistant"}
        ]
        return "\n\n".join(system_chunks), convo

    async def chat(
        self,
        messages: list[LLMMessage],
        *,
        temperature: float = 0.7,
        max_tokens: int = 1024,
    ) -> LLMResponse:
        assert self._client is not None
        system, convo = self._split(messages)
        resp = await self._client.messages.create(
            model=self._model,
            system=system or "You are a helpful assistant.",
            messages=convo,
            max_tokens=max_tokens,
            temperature=temperature,
        )
        text = "".join(block.text for block in resp.content if block.type == "text")
        return LLMResponse(
            content=text,
            model=self._model,
            usage={
                "input_tokens": resp.usage.input_tokens,
                "output_tokens": resp.usage.output_tokens,
            },
        )

    async def stream_chat(
        self,
        messages: list[LLMMessage],
        *,
        temperature: float = 0.7,
        max_tokens: int = 1024,
    ) -> AsyncIterator[str]:
        assert self._client is not None
        system, convo = self._split(messages)
        async with self._client.messages.stream(
            model=self._model,
            system=system or "You are a helpful assistant.",
            messages=convo,
            max_tokens=max_tokens,
            temperature=temperature,
        ) as stream:
            async for text in stream.text_stream:
                yield text
