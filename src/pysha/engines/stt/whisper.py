"""OpenAI Whisper (local) speech-to-text.

Runs entirely offline once the model is downloaded.  Install with::

    pip install 'pysha[stt-whisper]'
"""

from __future__ import annotations

import asyncio
import io
import wave
from typing import AsyncIterator

import structlog

from pysha.core.engine import Transcript

logger = structlog.get_logger(__name__)


class WhisperSTTEngine:
    """Local Whisper inference.  Uses the smallest model by default."""

    name = "whisper"

    def __init__(self, model: str = "base", sample_rate: int = 16000, **_: object) -> None:
        self._model_name = model
        self._sample_rate = sample_rate
        self._model = None

    async def start(self) -> None:
        try:
            import whisper  # type: ignore[import-not-found]
        except ImportError as exc:
            raise RuntimeError(
                "Install the STT extra:  pip install 'pysha[stt-whisper]'"
            ) from exc
        loop = asyncio.get_running_loop()
        self._model = await loop.run_in_executor(None, whisper.load_model, self._model_name)
        logger.info("stt.whisper.ready", model=self._model_name)

    async def stop(self) -> None:
        self._model = None

    async def transcribe(self, audio_bytes: bytes, *, language: str = "en") -> Transcript:
        import numpy as np

        assert self._model is not None
        # Assume 16-bit PCM mono at self._sample_rate
        audio = np.frombuffer(audio_bytes, dtype=np.int16).astype(np.float32) / 32768.0
        loop = asyncio.get_running_loop()
        result = await loop.run_in_executor(
            None, lambda: self._model.transcribe(audio, language=language)  # type: ignore[union-attr]
        )
        return Transcript(text=result["text"].strip(), language=language)

    async def stream(self, *, language: str = "en") -> AsyncIterator[Transcript]:
        try:
            import sounddevice as sd  # type: ignore[import-not-found]
        except ImportError as exc:
            raise RuntimeError(
                "Install the STT extra:  pip install 'pysha[stt-whisper]'"
            ) from exc

        chunk_seconds = 5
        sr = self._sample_rate
        loop = asyncio.get_running_loop()
        while True:
            recording = await loop.run_in_executor(
                None,
                lambda: sd.rec(
                    int(chunk_seconds * sr), samplerate=sr, channels=1, dtype="int16", blocking=True
                ),
            )
            buf = io.BytesIO()
            with wave.open(buf, "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(sr)
                wf.writeframes(recording.tobytes())
            try:
                yield await self.transcribe(recording.tobytes(), language=language)
            except Exception:
                logger.warning("stt.whisper.error", exc_info=True)
