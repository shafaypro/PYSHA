"""Rich-powered terminal UI."""

from __future__ import annotations

import asyncio

from rich.console import Console
from rich.markdown import Markdown
from rich.panel import Panel
from rich.prompt import Prompt
from rich.spinner import Spinner
from rich.text import Text

from pysha.app import Assistant


class CLI:
    def __init__(self, assistant: Assistant) -> None:
        self.assistant = assistant
        self.console = Console()

    def _banner(self) -> Panel:
        name = self.assistant.settings.assistant_name
        subtitle = (
            f"stt: {self.assistant.stt.name if self.assistant.stt else '—'}  · "
            f"tts: {self.assistant.tts.name if self.assistant.tts else '—'}  · "
            f"llm: {self.assistant.llm.name if self.assistant.llm else '—'}"
        )
        return Panel.fit(
            Text(f"{name} v2.0\n", style="bold cyan") + Text(subtitle, style="dim"),
            border_style="cyan",
        )

    async def chat_loop(self, *, speak: bool = False, voice: bool = False) -> None:
        self.console.print(self._banner())
        self.console.print(
            "[dim]Type your message, or :q to quit. Try 'weather in Paris' or 'tell me about Rome'.[/dim]\n"
        )
        if voice:
            await self._voice_loop(speak=True)
            return
        while True:
            try:
                text = Prompt.ask("[bold green]you[/bold green]")
            except (EOFError, KeyboardInterrupt):
                self.console.print("\n[yellow]goodbye[/yellow]")
                return
            if text.strip() in {":q", ":quit", "exit", "quit"}:
                return
            with self.console.status(Spinner("dots", text="thinking...")):
                reply = await self.assistant.handle_text(text)
            self.console.print(Panel(Markdown(reply), title="assistant", border_style="cyan"))
            if speak:
                asyncio.create_task(self.assistant.speak(reply))

    async def _voice_loop(self, *, speak: bool) -> None:
        if self.assistant.stt is None:
            self.console.print("[red]No STT engine configured.[/red]")
            return
        self.console.print("[green]Listening — say 'stop listening' to exit.[/green]")
        async for transcript in self.assistant.stt.stream(
            language=self.assistant.settings.stt_language
        ):
            text = transcript.text.strip()
            if not text:
                continue
            self.console.print(f"[bold green]you[/bold green]: {text}")
            if "stop listening" in text.lower():
                return
            reply = await self.assistant.handle_text(text)
            self.console.print(Panel(Markdown(reply), title="assistant", border_style="cyan"))
            if speak:
                await self.assistant.speak(reply)
