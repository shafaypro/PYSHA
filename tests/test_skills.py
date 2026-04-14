"""Skill-layer tests."""

from __future__ import annotations

import pytest

from pysha.core.memory import ConversationMemory, MemoryStore
from pysha.skills.base import SkillContext
from pysha.skills.datetime_skill import DateTimeSkill


@pytest.mark.asyncio
async def test_datetime_time_response(tmp_path):
    store = MemoryStore(tmp_path / "t.db")
    await store.open()
    ctx = SkillContext(utterance="what's the time?", memory=ConversationMemory(), store=store)
    result = await DateTimeSkill().handle(ctx)
    assert result.handled
    assert "It's" in result.response
    await store.close()


@pytest.mark.asyncio
async def test_datetime_date_response(tmp_path):
    store = MemoryStore(tmp_path / "t.db")
    await store.open()
    ctx = SkillContext(utterance="what's the date today?", memory=ConversationMemory(), store=store)
    result = await DateTimeSkill().handle(ctx)
    assert "Today is" in result.response
    await store.close()
