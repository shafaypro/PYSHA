"""Microsoft Edge Text-to-Speech (high-quality neural voices, free).

Install with: ``pip install 'pysha[tts-edge]'``
"""

from __future__ import annotations

import asyncio
import io
import tempfile
from pathlib import Path

import structlog

logger = structlog.get_logger(__name__)


class EdgeTTSEngine:
    """Neural TTS powered by Microsoft Edge's online service."""

    name = "edge"

    def __init__(
        self,
        voice: str = "en-US-AriaNeural",
        rate: str = "+0%",
        **_: object,
    ) -> None:
        self._voice = voice
        self._rate = rate

    async def start(self) -> None:
        try:
            import edge_tts  # noqa: F401 — import guarded here
        except ImportError as exc:
            raise RuntimeError(
                "Install the TTS extra:  pip install 'pysha[tts-edge]'"
            ) from exc
        logger.info("tts.edge.ready", voice=self._voice)

    async def stop(self) -> None: ...

    async def synthesize(self, text: str) -> bytes:
        import edge_tts  # type: ignore[import-not-found]

        communicate = edge_tts.Communicate(text, self._voice, rate=self._rate)
        buffer = io.BytesIO()
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                buffer.write(chunk["data"])
        return buffer.getvalue()

    async def speak(self, text: str) -> None:
        audio = await self.synthesize(text)
        await _play_mp3(audio)


async def _play_mp3(data: bytes) -> None:
    """Play MP3 data through the system's default player."""
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as f:
        tmp = Path(f.name)
        tmp.write_bytes(data)
    try:
        # Try multiple backends — users only need ONE of them installed.
        for backend in (_play_with_playsound, _play_with_pygame, _play_with_system):
            try:
                await backend(tmp)
                return
            except Exception:
                continue
        logger.warning("tts.edge.no_audio_backend", hint="install playsound or pygame")
    finally:
        tmp.unlink(missing_ok=True)


async def _play_with_playsound(path: Path) -> None:
    from playsound import playsound  # type: ignore[import-not-found]

    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, playsound, str(path))


async def _play_with_pygame(path: Path) -> None:
    import pygame  # type: ignore[import-not-found]

    loop = asyncio.get_running_loop()

    def _play() -> None:
        pygame.mixer.init()
        pygame.mixer.music.load(str(path))
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)

    await loop.run_in_executor(None, _play)


async def _play_with_system(path: Path) -> None:
    import shutil

    for cmd in ("mpg123", "ffplay", "afplay"):  # Linux, ffmpeg, macOS
        if shutil.which(cmd):
            args = [cmd]
            if cmd == "ffplay":
                args += ["-nodisp", "-autoexit"]
            args.append(str(path))
            proc = await asyncio.create_subprocess_exec(
                *args,
                stdout=asyncio.subprocess.DEVNULL,
                stderr=asyncio.subprocess.DEVNULL,
            )
            await proc.wait()
            return
    raise RuntimeError("no system audio player found")
