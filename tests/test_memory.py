"""Memory and store tests."""

from __future__ import annotations

import pytest

from pysha.core.memory import SHORT_TERM_CAPACITY, ConversationMemory, MemoryStore


def test_short_term_window_respects_capacity():
    mem = ConversationMemory(system_prompt="sys")
    for i in range(SHORT_TERM_CAPACITY + 5):
        mem.add("user", f"msg-{i}")
    assert len(mem.recent()) == SHORT_TERM_CAPACITY


def test_to_llm_messages_prepends_system():
    mem = ConversationMemory(system_prompt="sys")
    mem.add("user", "hi")
    mem.add("assistant", "hello")
    msgs = mem.to_llm_messages()
    assert msgs[0].role == "system"
    assert msgs[-1].content == "hello"


def test_clear_empties_both_windows():
    mem = ConversationMemory()
    mem.add("user", "x")
    mem.clear()
    assert not mem.recent()
    assert len(mem) == 0


@pytest.mark.asyncio
async def test_store_persists_and_retrieves_session(tmp_path):
    store = MemoryStore(tmp_path / "t.sqlite3")
    await store.open()
    await store.save_message("sess1", "user", "hi")
    await store.save_message("sess1", "assistant", "hey")
    rows = await store.load_session("sess1")
    await store.close()
    assert [r["role"] for r in rows] == ["user", "assistant"]


@pytest.mark.asyncio
async def test_store_facts_upsert(tmp_path):
    store = MemoryStore(tmp_path / "f.sqlite3")
    await store.open()
    await store.set_fact("user_name", "Shafay")
    await store.set_fact("user_name", "Amjad")
    assert await store.get_fact("user_name") == "Amjad"
    assert await store.get_fact("missing") is None
    await store.close()
