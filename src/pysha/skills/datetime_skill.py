"""Time and date queries."""

from __future__ import annotations

from datetime import datetime

from pysha.skills.base import Skill, SkillContext, SkillResult


class DateTimeSkill:
    name = "datetime"
    description = "Tells the current local time, date, or day of the week."
    triggers = [
        r"\bwhat('?s| is) the time\b",
        r"\bcurrent time\b",
        r"\bwhat('?s| is) the date\b",
        r"\btoday'?s date\b",
        r"\bwhat day is it\b",
    ]

    async def handle(self, ctx: SkillContext) -> SkillResult:
        now = datetime.now()
        lowered = ctx.utterance.lower()
        if "time" in lowered:
            return SkillResult(response=f"It's {now.strftime('%I:%M %p')}.")
        if "day" in lowered and "date" not in lowered:
            return SkillResult(response=f"Today is {now.strftime('%A')}.")
        return SkillResult(response=f"Today is {now.strftime('%A, %B %d, %Y')}.")


# Ensure the class satisfies the Skill protocol at import time.
_: Skill = DateTimeSkill()
