"""Skill contract shared by all built-in and third-party skills.

A *skill* is a self-contained capability — weather lookup, web search, media
control, system automation, etc.  The assistant's orchestrator asks the LLM
to decide which skill to invoke based on the user's utterance.

Skills are discovered automatically through the ``pysha.skills`` entry-point
group, so external authors can ship their own skill packages without forking
PYSHA.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any, Protocol, runtime_checkable

if TYPE_CHECKING:
    from pysha.core.memory import ConversationMemory, MemoryStore


@dataclass(slots=True)
class SkillContext:
    """Runtime context passed to a skill's ``handle`` method."""

    utterance: str
    memory: ConversationMemory
    store: MemoryStore
    extras: dict[str, Any] = field(default_factory=dict)


@dataclass(slots=True)
class SkillResult:
    """Structured response from a skill."""

    response: str
    handled: bool = True
    data: dict[str, Any] = field(default_factory=dict)


@runtime_checkable
class Skill(Protocol):
    """Contract every skill must satisfy."""

    @property
    def name(self) -> str: ...

    @property
    def description(self) -> str:
        """One-line description — shown to the LLM for intent routing."""
        ...

    @property
    def triggers(self) -> list[str]:
        """Regex/keyword patterns that match this skill (fast-path, pre-LLM)."""
        ...

    async def handle(self, ctx: SkillContext) -> SkillResult: ...
