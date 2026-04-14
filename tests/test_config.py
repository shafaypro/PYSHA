"""Config tests."""

from __future__ import annotations

import os

from pysha.config import Settings


def test_defaults():
    s = Settings()
    assert s.assistant_name == "PYSHA"
    assert s.stt_engine == "google"
    assert s.tts_engine == "edge"


def test_env_override(monkeypatch):
    monkeypatch.setenv("PYSHA_ASSISTANT_NAME", "Jarvis")
    monkeypatch.setenv("PYSHA_STT_ENGINE", "whisper")
    s = Settings()
    assert s.assistant_name == "Jarvis"
    assert s.stt_engine == "whisper"


def test_system_prompt_contains_name():
    s = Settings(assistant_name="Atlas")
    assert "Atlas" in s.system_prompt()


def test_resolved_data_dir_created(tmp_path, monkeypatch):
    target = tmp_path / "p"
    s = Settings(data_dir=target)
    resolved = s.resolved_data_dir
    assert resolved == target
    assert resolved.exists()
    _ = os.path  # keep import used
