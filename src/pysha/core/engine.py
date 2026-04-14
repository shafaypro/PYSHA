"""Engine protocols — the contracts that all STT, TTS, and LLM backends must satisfy.

Third-party or closed-source engines simply implement these protocols and register
themselves via the ``pysha.engines.*`` entry-point groups in their own
``pyproject.toml``.  No source-code changes to PYSHA are required.

Example (in a proprietary package's pyproject.toml)::

    [project.entry-points."pysha.engines.stt"]
    my_stt = "my_package.stt:MySTTEngine"
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Protocol, runtime_checkable

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

# ---------------------------------------------------------------------------
# Shared data types
# ---------------------------------------------------------------------------

@dataclass(frozen=True, slots=True)
class Transcript:
    """Result of a speech-to-text operation."""

    text: str
    confidence: float = 1.0
    language: str = "en"


@dataclass(frozen=True, slots=True)
class LLMMessage:
    """A single message in an LLM conversation."""

    role: str  # "system" | "user" | "assistant"
    content: str


@dataclass(slots=True)
class LLMResponse:
    """Response from an LLM engine."""

    content: str
    model: str = ""
    usage: dict[str, int] = field(default_factory=dict)


# ---------------------------------------------------------------------------
# Engine protocols
# ---------------------------------------------------------------------------

@runtime_checkable
class STTEngine(Protocol):
    """Speech-to-Text engine contract."""

    @property
    def name(self) -> str: ...

    async def start(self) -> None:
        """Initialize the engine (load models, open connections)."""
        ...

    async def stop(self) -> None:
        """Release resources."""
        ...

    async def transcribe(self, audio_bytes: bytes, *, language: str = "en") -> Transcript:
        """Transcribe a single audio buffer."""
        ...

    async def stream(self, *, language: str = "en") -> AsyncIterator[Transcript]:
        """Yield live transcription results from the microphone."""
        ...


@runtime_checkable
class TTSEngine(Protocol):
    """Text-to-Speech engine contract."""

    @property
    def name(self) -> str: ...

    async def start(self) -> None: ...
    async def stop(self) -> None: ...

    async def synthesize(self, text: str) -> bytes:
        """Return raw audio bytes (WAV/MP3) for the given text."""
        ...

    async def speak(self, text: str) -> None:
        """Play the synthesized speech through the default audio output."""
        ...


@runtime_checkable
class LLMEngine(Protocol):
    """Large Language Model engine contract."""

    @property
    def name(self) -> str: ...

    async def start(self) -> None: ...
    async def stop(self) -> None: ...

    async def chat(
        self,
        messages: list[LLMMessage],
        *,
        temperature: float = 0.7,
        max_tokens: int = 1024,
    ) -> LLMResponse:
        """Send a conversation and return the assistant's reply."""
        ...

    async def stream_chat(
        self,
        messages: list[LLMMessage],
        *,
        temperature: float = 0.7,
        max_tokens: int = 1024,
    ) -> AsyncIterator[str]:
        """Yield tokens as they arrive from the model."""
        ...
