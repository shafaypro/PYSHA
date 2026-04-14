"""Lightweight async event bus for decoupled communication between components."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Callable, Coroutine

import structlog

logger = structlog.get_logger(__name__)

Listener = Callable[["Event"], Coroutine[Any, Any, None]]


@dataclass(slots=True)
class Event:
    """A named event with arbitrary payload."""

    name: str
    data: dict[str, Any] = field(default_factory=dict)
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class EventBus:
    """Publish/subscribe event bus — all listeners run concurrently via ``asyncio``."""

    def __init__(self) -> None:
        self._listeners: dict[str, list[Listener]] = {}

    def on(self, event_name: str, callback: Listener) -> None:
        """Register *callback* to be invoked whenever *event_name* is emitted."""
        self._listeners.setdefault(event_name, []).append(callback)

    def off(self, event_name: str, callback: Listener) -> None:
        """Remove a previously registered listener."""
        if event_name in self._listeners:
            self._listeners[event_name] = [
                cb for cb in self._listeners[event_name] if cb is not callback
            ]

    async def emit(self, event: Event) -> None:
        """Dispatch *event* to all registered listeners (concurrently)."""
        listeners = self._listeners.get(event.name, []) + self._listeners.get("*", [])
        if not listeners:
            return
        logger.debug("event.emit", name=event.name, listener_count=len(listeners))
        await asyncio.gather(
            *(listener(event) for listener in listeners),
            return_exceptions=True,
        )
