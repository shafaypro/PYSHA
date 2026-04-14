"""Wolfram Alpha computation / fact skill.  Requires ``WOLFRAM_APP_ID``."""

from __future__ import annotations

import asyncio
import os

from pysha.skills.base import Skill, SkillContext, SkillResult


class WolframSkill:
    name = "wolfram"
    description = "Answers computational, scientific, and factual questions via Wolfram Alpha."
    triggers = [
        r"\bcompute (.+)",
        r"\bcalculate (.+)",
        r"\bconvert (.+)",
        r"\bsolve (.+)",
    ]

    def __init__(self, app_id: str | None = None, **_: object) -> None:
        self._app_id = app_id or os.getenv("PYSHA_WOLFRAM_APP_ID")

    async def handle(self, ctx: SkillContext) -> SkillResult:
        if not self._app_id:
            return SkillResult(
                response="Wolfram Alpha is not configured. Set PYSHA_WOLFRAM_APP_ID.",
                handled=True,
            )
        try:
            import wolframalpha  # type: ignore[import-not-found]
        except ImportError:
            return SkillResult(
                response="Install the Wolfram extra: pip install 'pysha[skills-wolfram]'.",
                handled=True,
            )
        client = wolframalpha.Client(self._app_id)
        loop = asyncio.get_running_loop()
        try:
            res = await loop.run_in_executor(None, client.query, ctx.utterance)
            answer = next(res.results).text  # type: ignore[attr-defined]
            return SkillResult(response=answer)
        except StopIteration:
            return SkillResult(response="Wolfram Alpha didn't return a result.")
        except Exception as exc:  # network, parse, etc.
            return SkillResult(response=f"Wolfram Alpha error: {exc}", handled=True)


_: Skill = WolframSkill()
