"""Event bus tests."""

from __future__ import annotations

import pytest

from pysha.core.events import Event, EventBus


@pytest.mark.asyncio
async def test_emit_invokes_registered_listener():
    bus = EventBus()
    received: list[Event] = []

    async def listener(event: Event) -> None:
        received.append(event)

    bus.on("ping", listener)
    await bus.emit(Event("ping", {"n": 1}))
    assert received[0].data == {"n": 1}


@pytest.mark.asyncio
async def test_wildcard_listener_receives_all_events():
    bus = EventBus()
    received: list[str] = []

    async def wildcard(event: Event) -> None:
        received.append(event.name)

    bus.on("*", wildcard)
    await bus.emit(Event("a"))
    await bus.emit(Event("b"))
    assert received == ["a", "b"]


@pytest.mark.asyncio
async def test_off_removes_listener():
    bus = EventBus()
    received: list[Event] = []

    async def listener(event: Event) -> None:
        received.append(event)

    bus.on("ping", listener)
    bus.off("ping", listener)
    await bus.emit(Event("ping"))
    assert received == []
