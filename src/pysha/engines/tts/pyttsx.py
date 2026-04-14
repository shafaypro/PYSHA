"""Offline text-to-speech via pyttsx3 (SAPI5 / NSSpeech / espeak).

Install with: ``pip install 'pysha[tts-pyttsx]'``
"""

from __future__ import annotations

import asyncio

import structlog

logger = structlog.get_logger(__name__)


class PyttsxTTSEngine:
    """Cross-platform offline TTS.  Quality is modest but 100% local."""

    name = "pyttsx"

    def __init__(self, voice: str | None = None, rate: int = 180, **_: object) -> None:
        self._voice = voice
        self._rate = rate
        self._engine = None

    async def start(self) -> None:
        try:
            import pyttsx3  # type: ignore[import-not-found]
        except ImportError as exc:
            raise RuntimeError(
                "Install the TTS extra:  pip install 'pysha[tts-pyttsx]'"
            ) from exc
        self._engine = pyttsx3.init()
        self._engine.setProperty("rate", self._rate)
        if self._voice:
            for v in self._engine.getProperty("voices"):
                if self._voice.lower() in v.name.lower() or self._voice == v.id:
                    self._engine.setProperty("voice", v.id)
                    break
        logger.info("tts.pyttsx.ready")

    async def stop(self) -> None:
        if self._engine is not None:
            self._engine.stop()
            self._engine = None

    async def synthesize(self, text: str) -> bytes:
        import tempfile
        from pathlib import Path

        assert self._engine is not None
        loop = asyncio.get_running_loop()
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            tmp = Path(f.name)
        try:
            await loop.run_in_executor(None, self._engine.save_to_file, text, str(tmp))
            await loop.run_in_executor(None, self._engine.runAndWait)
            return tmp.read_bytes()
        finally:
            tmp.unlink(missing_ok=True)

    async def speak(self, text: str) -> None:
        assert self._engine is not None
        loop = asyncio.get_running_loop()

        def _say() -> None:
            self._engine.say(text)  # type: ignore[union-attr]
            self._engine.runAndWait()  # type: ignore[union-attr]

        await loop.run_in_executor(None, _say)
