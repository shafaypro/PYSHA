"""PYSHA command-line interface."""

from __future__ import annotations

import asyncio

import click

from pysha import __version__
from pysha.app import Assistant
from pysha.config import load_settings
from pysha.utils.logging import configure_logging


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__, prog_name="pysha")
def cli() -> None:
    """PYSHA v2 — a modular, AI-powered virtual assistant."""


@cli.command("chat")
@click.option("--speak/--no-speak", default=False, help="Speak replies aloud.")
def chat_cmd(speak: bool) -> None:
    """Start an interactive text chat."""
    asyncio.run(_run_chat(speak=speak, voice=False))


@cli.command("listen")
def listen_cmd() -> None:
    """Start a voice-driven conversation using your microphone."""
    asyncio.run(_run_chat(speak=True, voice=True))


@cli.command("web")
@click.option("--host", default=None, help="Override host (default from config).")
@click.option("--port", default=None, type=int, help="Override port (default from config).")
def web_cmd(host: str | None, port: int | None) -> None:
    """Serve the web UI."""
    settings = load_settings()
    configure_logging(settings.log_level)
    try:
        import uvicorn
    except ImportError as exc:  # pragma: no cover
        raise click.ClickException("Install the web extra: pip install 'pysha[web]'") from exc
    from pysha.ui.web import build_app

    assistant = Assistant(settings)
    app = build_app(assistant)
    uvicorn.run(app, host=host or settings.web_host, port=port or settings.web_port)


@cli.command("plugins")
def plugins_cmd() -> None:
    """List discovered engines and skills."""
    from rich.console import Console
    from rich.table import Table

    from pysha.core.plugin import PluginLoader

    console = Console()
    for group in ("pysha.engines.stt", "pysha.engines.tts", "pysha.engines.llm", "pysha.skills"):
        table = Table(title=group, header_style="bold cyan")
        table.add_column("name")
        table.add_column("target")
        for name, ep in PluginLoader.list_plugins(group).items():
            table.add_row(name, ep.value)
        console.print(table)


async def _run_chat(*, speak: bool, voice: bool) -> None:
    settings = load_settings()
    configure_logging(settings.log_level)
    assistant = Assistant(settings)
    await assistant.start()
    try:
        from pysha.ui.cli import CLI

        await CLI(assistant).chat_loop(speak=speak, voice=voice)
    finally:
        await assistant.stop()


def main() -> None:
    cli()


if __name__ == "__main__":
    main()
