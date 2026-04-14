"""Pydantic-based configuration.

All settings can be supplied via environment variables (prefixed ``PYSHA_``)
or a ``.env`` file in the project root.  See ``.env.example`` for a template.
"""

from __future__ import annotations

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central configuration — immutable after load."""

    model_config = SettingsConfigDict(
        env_prefix="PYSHA_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    # --- Engine selection ---
    stt_engine: str = Field(default="google", description="Name of the STT plugin to use.")
    tts_engine: str = Field(default="edge", description="Name of the TTS plugin to use.")
    llm_engine: str = Field(default="anthropic", description="Name of the LLM plugin to use.")

    # --- LLM keys / endpoints ---
    anthropic_api_key: str | None = None
    openai_api_key: str | None = None
    ollama_base_url: str = "http://localhost:11434"

    # --- LLM models ---
    anthropic_model: str = "claude-sonnet-4-20250514"
    openai_model: str = "gpt-4o"
    ollama_model: str = "llama3.1"

    # --- Speech ---
    stt_language: str = "en-US"
    tts_voice: str = "en-US-AriaNeural"
    tts_rate: str = "+0%"

    # --- Skill keys ---
    wolfram_app_id: str | None = None
    deepgram_api_key: str | None = None

    # --- Web UI ---
    web_host: str = "127.0.0.1"
    web_port: int = 8000

    # --- General ---
    log_level: str = "INFO"
    assistant_name: str = "PYSHA"
    data_dir: Path = Field(default=Path("~/.pysha"))

    @property
    def resolved_data_dir(self) -> Path:
        """Expand ``~`` and ensure the directory exists."""
        path = self.data_dir.expanduser()
        path.mkdir(parents=True, exist_ok=True)
        return path

    @property
    def db_path(self) -> Path:
        return self.resolved_data_dir / "pysha.sqlite3"

    def system_prompt(self) -> str:
        return (
            f"You are {self.assistant_name}, a helpful, concise, voice-first virtual assistant. "
            "Reply in natural spoken language — avoid markdown, bullet points, and code unless "
            "the user explicitly asks.  Keep answers under three sentences when possible.  "
            "If a user asks for an action you cannot perform, say so briefly."
        )


def load_settings() -> Settings:
    """Load settings from env + .env.  Cached by convention at module level."""
    return Settings()
