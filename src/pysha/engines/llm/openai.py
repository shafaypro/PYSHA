"""OpenAI GPT engine.

Install with: ``pip install 'pysha[llm-openai]'``
"""

from __future__ import annotations

from typing import TYPE_CHECKING

import structlog

from pysha.core.engine import LLMMessage, LLMResponse

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

logger = structlog.get_logger(__name__)


class OpenAILLMEngine:
    name = "openai"

    def __init__(
        self,
        api_key: str | None = None,
        model: str = "gpt-4o",
        **_: object,
    ) -> None:
        self._api_key = api_key
        self._model = model
        self._client = None

    async def start(self) -> None:
        try:
            from openai import AsyncOpenAI  # type: ignore[import-not-found]
        except ImportError as exc:
            raise RuntimeError(
                "Install the LLM extra:  pip install 'pysha[llm-openai]'"
            ) from exc
        self._client = AsyncOpenAI(api_key=self._api_key)
        logger.info("llm.openai.ready", model=self._model)

    async def stop(self) -> None:
        if self._client is not None:
            await self._client.close()
            self._client = None

    async def chat(
        self,
        messages: list[LLMMessage],
        *,
        temperature: float = 0.7,
        max_tokens: int = 1024,
    ) -> LLMResponse:
        assert self._client is not None
        resp = await self._client.chat.completions.create(
            model=self._model,
            messages=[{"role": m.role, "content": m.content} for m in messages],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        choice = resp.choices[0]
        return LLMResponse(
            content=choice.message.content or "",
            model=self._model,
            usage={
                "prompt_tokens": resp.usage.prompt_tokens if resp.usage else 0,
                "completion_tokens": resp.usage.completion_tokens if resp.usage else 0,
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
        stream = await self._client.chat.completions.create(
            model=self._model,
            messages=[{"role": m.role, "content": m.content} for m in messages],
            temperature=temperature,
            max_tokens=max_tokens,
            stream=True,
        )
        async for chunk in stream:
            delta = chunk.choices[0].delta.content
            if delta:
                yield delta
