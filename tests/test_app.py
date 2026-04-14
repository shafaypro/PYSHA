"""End-to-end assistant routing tests (no network / no hardware)."""

from __future__ import annotations

import pytest


@pytest.mark.asyncio
async def test_handle_text_falls_back_to_llm(assistant):
    reply = await assistant.handle_text("tell me a story about cats")
    # The datetime/weather etc. regexes won't match, so LLM is used.
    assert reply == "fake-reply"


@pytest.mark.asyncio
async def test_handle_text_routes_to_datetime_skill(assistant):
    reply = await assistant.handle_text("what's the time?")
    assert "It's" in reply


@pytest.mark.asyncio
async def test_conversation_memory_grows(assistant):
    await assistant.handle_text("hi")
    await assistant.handle_text("hello again")
    assert len(assistant.memory) == 4  # 2 user + 2 assistant
