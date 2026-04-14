"""Conversation memory and persistent storage.

Carries forward the original PYSHA's "7 ± 2" short-term memory concept while
adding long-term persistence backed by SQLite (async via aiosqlite).
"""

from __future__ import annotations

import json
from collections import deque
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import aiosqlite
import structlog

from pysha.core.engine import LLMMessage

logger = structlog.get_logger(__name__)

SHORT_TERM_CAPACITY = 7  # Miller's Law — 7 ± 2


@dataclass(slots=True)
class MemoryEntry:
    role: str
    content: str
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class ConversationMemory:
    """Short-term sliding window + full conversation history for LLM context."""

    def __init__(self, system_prompt: str = "", capacity: int = SHORT_TERM_CAPACITY) -> None:
        self._system_prompt = system_prompt
        self._capacity = capacity
        self._short_term: deque[MemoryEntry] = deque(maxlen=capacity)
        self._history: list[MemoryEntry] = []

    @property
    def system_prompt(self) -> str:
        return self._system_prompt

    @system_prompt.setter
    def system_prompt(self, value: str) -> None:
        self._system_prompt = value

    def add(self, role: str, content: str) -> None:
        entry = MemoryEntry(role=role, content=content)
        self._short_term.append(entry)
        self._history.append(entry)

    def recent(self) -> list[MemoryEntry]:
        """Return the short-term window (last *capacity* exchanges)."""
        return list(self._short_term)

    def to_llm_messages(self, *, include_system: bool = True) -> list[LLMMessage]:
        """Build the message list to send to an LLM."""
        messages: list[LLMMessage] = []
        if include_system and self._system_prompt:
            messages.append(LLMMessage(role="system", content=self._system_prompt))
        for entry in self._short_term:
            messages.append(LLMMessage(role=entry.role, content=entry.content))
        return messages

    def clear(self) -> None:
        self._short_term.clear()
        self._history.clear()

    def __len__(self) -> int:
        return len(self._history)


class MemoryStore:
    """Async SQLite-backed persistent memory for conversations, queries, and facts."""

    def __init__(self, db_path: Path) -> None:
        self._db_path = db_path
        self._db: aiosqlite.Connection | None = None

    async def open(self) -> None:
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
        self._db = await aiosqlite.connect(str(self._db_path))
        await self._db.execute("""
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT NOT NULL,
                role TEXT NOT NULL,
                content TEXT NOT NULL,
                metadata TEXT DEFAULT '{}',
                created_at TEXT NOT NULL DEFAULT (datetime('now'))
            )
        """)
        await self._db.execute("""
            CREATE TABLE IF NOT EXISTS facts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                key TEXT UNIQUE NOT NULL,
                value TEXT NOT NULL,
                updated_at TEXT NOT NULL DEFAULT (datetime('now'))
            )
        """)
        await self._db.commit()
        logger.info("memory_store.opened", path=str(self._db_path))

    async def close(self) -> None:
        if self._db:
            await self._db.close()
            self._db = None

    async def save_message(
        self, session_id: str, role: str, content: str, metadata: dict | None = None
    ) -> None:
        assert self._db is not None
        await self._db.execute(
            "INSERT INTO conversations (session_id, role, content, metadata) VALUES (?, ?, ?, ?)",
            (session_id, role, content, json.dumps(metadata or {})),
        )
        await self._db.commit()

    async def load_session(self, session_id: str, limit: int = 50) -> list[dict]:
        assert self._db is not None
        cursor = await self._db.execute(
            "SELECT role, content, metadata, created_at FROM conversations "
            "WHERE session_id = ? ORDER BY id DESC LIMIT ?",
            (session_id, limit),
        )
        rows = await cursor.fetchall()
        return [
            {"role": r[0], "content": r[1], "metadata": json.loads(r[2]), "created_at": r[3]}
            for r in reversed(rows)
        ]

    async def set_fact(self, key: str, value: str) -> None:
        assert self._db is not None
        await self._db.execute(
            "INSERT INTO facts (key, value, updated_at) VALUES (?, ?, datetime('now')) "
            "ON CONFLICT(key) DO UPDATE SET value = excluded.value, updated_at = excluded.updated_at",
            (key, value),
        )
        await self._db.commit()

    async def get_fact(self, key: str) -> str | None:
        assert self._db is not None
        cursor = await self._db.execute("SELECT value FROM facts WHERE key = ?", (key,))
        row = await cursor.fetchone()
        return row[0] if row else None
