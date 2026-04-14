# Authoring plugins for PYSHA

PYSHA is intentionally unopinionated about *what* engines or skills it runs.
Every extension point is a Python **entry-point group**, so a third-party
package — open-source or proprietary — can register an implementation without
modifying PYSHA itself.

## Entry-point groups

| Group | Protocol | Purpose |
|---|---|---|
| `pysha.engines.stt` | `pysha.core.engine.STTEngine` | Speech-to-text backend |
| `pysha.engines.tts` | `pysha.core.engine.TTSEngine` | Text-to-speech backend |
| `pysha.engines.llm` | `pysha.core.engine.LLMEngine` | Language-model backend |
| `pysha.skills` | `pysha.skills.base.Skill` | High-level capability / command |

## Contract

All engines and skills are Python **Protocols** — no subclassing required; you
just need to provide the methods.  The core library never imports your module
directly; it resolves it from the entry-point registry at runtime.

## A complete skill example

```python
# coolcorp_skills/joke.py
import random
from pysha.skills.base import Skill, SkillContext, SkillResult

class JokeSkill:
    name = "joke"
    description = "Tells a (dad-grade) joke."
    triggers = [r"\btell me a joke\b", r"\bmake me laugh\b"]

    _JOKES = ["Why did the dev go broke? They lost their cache."]

    async def handle(self, ctx: SkillContext) -> SkillResult:
        return SkillResult(response=random.choice(self._JOKES))

_: Skill = JokeSkill()   # static protocol check at import time
```

```toml
# coolcorp_skills/pyproject.toml
[project.entry-points."pysha.skills"]
joke = "coolcorp_skills.joke:JokeSkill"
```

## A closed-source STT engine

```python
# acme_stt/engine.py
from pysha.core.engine import STTEngine, Transcript

class AcmeSTT:
    name = "acme"
    def __init__(self, api_key: str | None = None, **_): self._key = api_key
    async def start(self): ...
    async def stop(self): ...
    async def transcribe(self, audio, *, language="en") -> Transcript:
        # proprietary network call
        return Transcript(text="…")
    async def stream(self, *, language="en"):
        yield Transcript(text="…")
```

```toml
[project.entry-points."pysha.engines.stt"]
acme = "acme_stt.engine:AcmeSTT"
```

The package can be distributed as a proprietary wheel under any license.
PYSHA's MIT license applies *only* to `src/pysha/`, not to your wheel.

## Configuration passthrough

The assistant forwards a fixed set of kwargs from settings to each engine:

- STT: `language`
- TTS: `voice`, `rate`
- LLM: `api_key`, `model`, `base_url` (depending on engine name)

Your engine's `__init__` must accept `**kwargs` (or just the keys you care
about plus `**_`) to stay forward-compatible.

## Discovery / verification

```bash
pysha plugins
```

Shows every engine and skill PYSHA can see, along with its import target.
If yours is missing, double-check that the owning package is installed into
the same interpreter and that the entry-point group name is spelled correctly.
