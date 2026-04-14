"""Wikipedia lookup skill."""

from __future__ import annotations

import asyncio
import re

from pysha.skills.base import Skill, SkillContext, SkillResult


class WikipediaSkill:
    name = "wikipedia"
    description = "Looks up a topic on Wikipedia and returns a short summary."
    triggers = [
        r"\bwikipedia (.+)",
        r"\b(?:who|what) (?:is|was|are|were) (.+)",
        r"\btell me about (.+)",
    ]

    async def handle(self, ctx: SkillContext) -> SkillResult:
        try:
            import wikipedia  # type: ignore[import-not-found]
        except ImportError:
            return SkillResult(
                response="Install the Wikipedia extra: pip install 'pysha[skills-wikipedia]'.",
                handled=True,
            )
        topic = self._extract_topic(ctx.utterance)
        if not topic:
            return SkillResult(response="What topic should I look up?")
        loop = asyncio.get_running_loop()
        try:
            summary = await loop.run_in_executor(
                None, lambda: wikipedia.summary(topic, sentences=2, auto_suggest=True)
            )
            return SkillResult(response=summary, data={"topic": topic})
        except wikipedia.DisambiguationError as exc:
            options = ", ".join(exc.options[:3])
            return SkillResult(response=f"Did you mean one of these: {options}?")
        except wikipedia.PageError:
            return SkillResult(response=f"I couldn't find a Wikipedia page for {topic}.")

    @staticmethod
    def _extract_topic(utterance: str) -> str:
        for pattern in (
            r"\bwikipedia (.+)",
            r"\btell me about (.+)",
            r"\b(?:who|what) (?:is|was|are|were) (.+)",
        ):
            m = re.search(pattern, utterance, re.IGNORECASE)
            if m:
                return m.group(1).strip(" ?.!")
        return utterance


_: Skill = WikipediaSkill()
