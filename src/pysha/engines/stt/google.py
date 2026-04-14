"""Google Speech Recognition STT (via the ``SpeechRecognition`` package).

Optional dependency — install with ``pip install 'pysha[stt-google]'``.
"""

from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

import structlog

from pysha.core.engine import Transcript

if TYPE_CHECKING:
    from collections.abc import AsyncIterator

logger = structlog.get_logger(__name__)


class GoogleSTTEngine:
    """Uses the free Google Web Speech endpoint (rate-limited) for transcription."""

    name = "google"

    def __init__(self, language: str = "en-US", **_: object) -> None:
        self._language = language
        self._recognizer = None
        self._microphone = None

    async def start(self) -> None:
        try:
            import speech_recognition as sr  # type: ignore[import-not-found]
        except ImportError as exc:
            raise RuntimeError(
                "Install the STT extra:  pip install 'pysha[stt-google]'"
            ) from exc
        self._recognizer = sr.Recognizer()
        self._microphone = sr.Microphone()
        with self._microphone as source:
            self._recognizer.adjust_for_ambient_noise(source, duration=0.5)
        logger.info("stt.google.ready", language=self._language)

    async def stop(self) -> None:
        self._recognizer = None
        self._microphone = None

    async def transcribe(self, audio_bytes: bytes, *, language: str = "en-US") -> Transcript:
        import speech_recognition as sr  # type: ignore[import-not-found]

        assert self._recognizer is not None
        audio = sr.AudioData(audio_bytes, sample_rate=16000, sample_width=2)
        loop = asyncio.get_running_loop()
        text = await loop.run_in_executor(
            None,
            lambda: self._recognizer.recognize_google(audio, language=language),  # type: ignore[union-attr]
        )
        return Transcript(text=text, language=language)

    async def stream(self, *, language: str = "en-US") -> AsyncIterator[Transcript]:
        import speech_recognition as sr  # type: ignore[import-not-found]

        assert self._recognizer is not None and self._microphone is not None
        loop = asyncio.get_running_loop()
        while True:
            with self._microphone as source:
                audio = await loop.run_in_executor(
                    None, lambda: self._recognizer.listen(source, phrase_time_limit=10)  # type: ignore[union-attr]
                )
            try:
                text = await loop.run_in_executor(
                    None,
                    lambda audio=audio: self._recognizer.recognize_google(  # type: ignore[union-attr]
                        audio,
                        language=language,
                    ),
                )
                yield Transcript(text=text, language=language)
            except sr.UnknownValueError:
                continue
            except sr.RequestError as exc:
                logger.warning("stt.google.request_error", error=str(exc))
                await asyncio.sleep(1.0)
