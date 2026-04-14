"""Web search via DuckDuckGo (no API key required)."""

from __future__ import annotations

import re

from pysha.skills.base import Skill, SkillContext, SkillResult


class WebSearchSkill:
    name = "web_search"
    description = "Searches the web and summarizes the top result."
    triggers = [
        r"\bsearch (?:for |the web for )?(.+)",
        r"\bgoogle (.+)",
        r"\blook up (.+)",
    ]

    async def handle(self, ctx: SkillContext) -> SkillResult:
        try:
            from duckduckgo_search import DDGS  # type: ignore[import-not-found]
        except ImportError:
            return SkillResult(
                response="Install the web-search extra: pip install 'pysha[skills-web]'.",
                handled=True,
            )
        query = self._extract_query(ctx.utterance)
        if not query:
            return SkillResult(response="What should I search for?", handled=True)
        results = list(DDGS().text(query, max_results=3))
        if not results:
            return SkillResult(response=f"I couldn't find anything about {query}.")
        top = results[0]
        return SkillResult(
            response=f"Here's what I found: {top.get('body', top.get('title', ''))}",
            data={"results": results, "query": query},
        )

    @staticmethod
    def _extract_query(utterance: str) -> str:
        for pattern in (
            r"\b(?:search for|search the web for|search|google|look up)\s+(.+)",
        ):
            m = re.search(pattern, utterance, re.IGNORECASE)
            if m:
                return m.group(1).strip(" ?.!")
        return utterance


_: Skill = WebSearchSkill()
