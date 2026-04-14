# PYSHA v2

> **A modular, AI-powered virtual assistant with pluggable engines for speech, language, and automation.**

[![CI](https://github.com/shafaypro/pysha/actions/workflows/ci.yml/badge.svg)](https://github.com/shafaypro/pysha/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.11%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

PYSHA started in 2017 as a student project stitched together around Google STT,
`pyttsx`, ChatterBot, and a hundred small HTML-scraping hacks.  Version 2 is a
ground-up rewrite that keeps the original spirit — a voice-first, pluggable,
"do-stuff-for-me" assistant — but modernises every layer: async Python 3.11+,
LLM-powered conversation, neural TTS, Whisper STT, a typed plugin system, a
FastAPI web UI, a Rich terminal UI, and Docker packaging.

---

## Highlights

- **LLM-powered** — drop-in support for **Anthropic Claude**, **OpenAI GPT**,
  or local models via **Ollama**.
- **Modular engines** — every STT, TTS, and LLM backend is a plugin.
- **Open core, closed extensions** — third-party engines can ship under any
  license via Python entry-points. No fork required.
- **Skill-based commands** — weather, Wikipedia, Wolfram Alpha, web search,
  news, system control, date/time. Add your own with ~30 lines of code.
- **Voice or text** — speak to it, type to it, or call it from HTTP / WebSocket.
- **Persistent + short-term memory** — async SQLite long-term store plus a
  7-item sliding context window (a nod to Miller's Law, carried over from v1).
- **First-class observability** — structured logging (`structlog`) and an
  async event bus for UIs and telemetry.
- **Typed, tested, packaged** — Pydantic settings, `pyproject.toml`,
  `pytest`/`ruff`/`mypy`, Docker, GitHub Actions.

---

## Architecture

```
┌────────────────┐   text / voice   ┌────────────────────────────────────┐
│  CLI / Web UI  │ ────────────────▶│            Assistant               │
└────────────────┘                  │  (orchestrator + EventBus + memory)│
                                    └──────┬──────────────┬──────────────┘
                                           │              │
                 ┌─────────────────────────┤              ├─────────────────┐
                 ▼                         ▼              ▼                 ▼
          ┌────────────┐           ┌──────────────┐ ┌───────────┐   ┌───────────────┐
          │ STT Engine │           │  TTS Engine  │ │ LLM Engine│   │    Skills     │
          │ (protocol) │           │  (protocol)  │ │ (protocol)│   │  (protocol)   │
          └────────────┘           └──────────────┘ └───────────┘   └───────────────┘
          whisper · google           edge · pyttsx   anthropic        weather · news
          *your-engine*              *your-engine*   openai · ollama  wikipedia · …
                                                     *your-engine*    *your-skill*
```

Everything below the protocol line is a **plugin** discovered at runtime via
entry-point groups. The assistant itself never imports a specific engine.

---

## Quickstart

### 1. Install

```bash
# Clone, create a venv, install the open-source defaults + a Claude backend:
git clone https://github.com/shafaypro/pysha && cd pysha
python -m venv .venv && source .venv/bin/activate
pip install -e ".[llm-anthropic,tts-edge,skills-web,skills-wikipedia,skills-news]"
```

### 2. Configure

```bash
cp .env.example .env
# edit .env — set PYSHA_ANTHROPIC_API_KEY at minimum.
```

### 3. Run

```bash
pysha chat          # text chat in your terminal
pysha chat --speak  # also speaks replies aloud
pysha listen        # voice conversation via microphone
pysha web           # FastAPI + WebSocket UI at http://127.0.0.1:8000
pysha plugins       # show every discovered engine / skill
```

---

## Configuration

All settings are environment variables with the `PYSHA_` prefix, or in a
`.env` file in the working directory.

| Key | Default | Description |
|---|---|---|
| `PYSHA_STT_ENGINE` | `google` | STT plugin name |
| `PYSHA_TTS_ENGINE` | `edge` | TTS plugin name |
| `PYSHA_LLM_ENGINE` | `anthropic` | LLM plugin name |
| `PYSHA_ANTHROPIC_API_KEY` | — | Claude API key |
| `PYSHA_OPENAI_API_KEY` | — | OpenAI API key |
| `PYSHA_OLLAMA_BASE_URL` | `http://localhost:11434` | Local Ollama host |
| `PYSHA_TTS_VOICE` | `en-US-AriaNeural` | Edge TTS voice |
| `PYSHA_WOLFRAM_APP_ID` | — | Wolfram Alpha key |
| `PYSHA_WEB_HOST` / `PYSHA_WEB_PORT` | `127.0.0.1:8000` | Web UI bind |

See `src/pysha/config.py` for the full list.

---

## Writing a plugin (open or closed source)

PYSHA's core is MIT-licensed. **Your plugin is not.**  You can ship it under any
license you like — GPL, Apache, proprietary, commercial — and PYSHA will discover
it automatically if you declare an entry-point.

### Example: a custom STT engine

```python
# my_package/stt.py
from pysha.core.engine import STTEngine, Transcript

class MyCompanySTT:
    name = "my-company-stt"

    async def start(self):  ...
    async def stop(self):   ...

    async def transcribe(self, audio_bytes, *, language="en") -> Transcript:
        # call your proprietary service here
        return Transcript(text="hello world")

    async def stream(self, *, language="en"):
        yield Transcript(text="streamed chunk")
```

```toml
# my_package/pyproject.toml
[project.entry-points."pysha.engines.stt"]
my-company-stt = "my_package.stt:MyCompanySTT"
```

Then:

```bash
pip install my-package                 # your proprietary wheel
PYSHA_STT_ENGINE=my-company-stt pysha chat
```

The same pattern works for `pysha.engines.tts`, `pysha.engines.llm`, and
`pysha.skills`.  See `docs/PLUGINS.md` for a full authoring guide.

---

## Skills

Built-in skills (all optional, installed with extras):

| Skill | Trigger examples | Extra |
|---|---|---|
| `datetime_skill` | *"what's the time?"* · *"today's date"* | — |
| `weather` | *"weather in Paris"* · *"temperature in Tokyo"* | — (uses Open-Meteo) |
| `wikipedia` | *"tell me about quantum physics"* | `skills-wikipedia` |
| `web_search` | *"search for site reliability engineering"* | `skills-web` |
| `news` | *"what's in the news?"* · *"headlines"* | `skills-news` |
| `wolfram` | *"compute integral of sin(x) dx"* | `skills-wolfram` |
| `system_control` | *"open calculator"* · *"close chrome"* | `skills-system` |

Unmatched utterances fall through to the configured LLM.

---

## Docker

```bash
docker build -t pysha .
docker run --rm -it --env-file .env -p 8000:8000 pysha
# or
docker compose up
```

---

## Development

```bash
pip install -e ".[dev]"
ruff check src tests
pytest -q
```

```
src/pysha/
├── __main__.py          # CLI entry
├── app.py               # Assistant orchestrator
├── config.py            # Pydantic settings
├── core/                # Protocols, plugin loader, event bus, memory
├── engines/
│   ├── stt/             # whisper, google, (your-engine)
│   ├── tts/             # edge, pyttsx, (your-engine)
│   └── llm/             # anthropic, openai, ollama, (your-engine)
├── skills/              # datetime, weather, wikipedia, wolfram, …
├── ui/                  # cli.py (Rich), web.py (FastAPI)
└── utils/
```

---

## Migrating from v1

The v1 monolith (2123-line `__PYSHA.py` et al.) has been preserved under
[`legacy/`](./legacy/) so old behaviours remain inspectable and reusable.
Features you relied on in v1 map to v2 as follows:

| v1 module | v2 equivalent |
|---|---|
| `__Voice.py` + `pyttsx` | `engines.tts.edge` / `engines.tts.pyttsx` |
| `speech_recognition` | `engines.stt.google` / `engines.stt.whisper` |
| `ChatterBot` corpus | LLM (Anthropic / OpenAI / Ollama) |
| `_WolFrameAlphaClass.py` | `skills.wolfram` |
| `_YouTube.py`, `__github.py`, … | `skills.web_search` (or custom skill) |
| `__shorttermmemory.py` (7 ± 2) | `core.memory.ConversationMemory` |
| `_dbdata.py` (SQLite) | `core.memory.MemoryStore` (async) |
| Tkinter `__init__.py` | `ui.cli` (Rich) + `ui.web` (FastAPI) |

---

## Licensing

- **Core (this repository):** MIT — free for open-source and commercial use.
- **Plugins:** author's choice.  Proprietary, closed-source engines are a
  first-class citizen: install the wheel, set the env var, run PYSHA.

See [`LICENSE`](./LICENSE) for the full dual-licensing notice.

---

## Credits

Originally created in 2017 by **Shafay** as an undergraduate project.
v2.0 is a modernising rewrite — new stack, new architecture, same spirit.
