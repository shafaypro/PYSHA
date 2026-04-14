"""Headline-news skill — pulls top stories via DuckDuckGo News."""

from __future__ import annotations

from pysha.skills.base import Skill, SkillContext, SkillResult


class NewsSkill:
    name = "news"
    description = "Reads the latest news headlines."
    triggers = [
        r"\b(?:latest |top )?news\b",
        r"\bheadlines\b",
        r"\bwhat'?s happening\b",
    ]

    async def handle(self, ctx: SkillContext) -> SkillResult:
        try:
            from duckduckgo_search import DDGS  # type: ignore[import-not-found]
        except ImportError:
            return SkillResult(
                response="Install the news extra: pip install 'pysha[skills-news]'.",
                handled=True,
            )
        items = list(DDGS().news("top news", max_results=5))
        if not items:
            return SkillResult(response="I couldn't find any news right now.")
        headlines = [item.get("title", "") for item in items[:3]]
        spoken = " ... ".join(h for h in headlines if h)
        return SkillResult(response=f"Here are the top stories: {spoken}.", data={"items": items})


_: Skill = NewsSkill()
