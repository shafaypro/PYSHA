"""Weather skill — uses the free Open-Meteo API (no key required)."""

from __future__ import annotations

import re

import httpx

from pysha.skills.base import Skill, SkillContext, SkillResult


class WeatherSkill:
    name = "weather"
    description = "Reports current weather for a city using Open-Meteo."
    triggers = [
        r"\bweather (?:in |for )?(.+)",
        r"\b(?:how'?s|what'?s) the weather (?:in |for )?(.+)?",
        r"\btemperature (?:in |for )?(.+)",
    ]

    async def handle(self, ctx: SkillContext) -> SkillResult:
        city = self._extract_city(ctx.utterance)
        if not city:
            return SkillResult(response="Which city should I check?")
        async with httpx.AsyncClient(timeout=10) as client:
            geo = await client.get(
                "https://geocoding-api.open-meteo.com/v1/search",
                params={"name": city, "count": 1, "language": "en", "format": "json"},
            )
            geo.raise_for_status()
            data = geo.json().get("results") or []
            if not data:
                return SkillResult(response=f"I don't know where {city} is.")
            lat, lon, resolved = data[0]["latitude"], data[0]["longitude"], data[0]["name"]
            weather = await client.get(
                "https://api.open-meteo.com/v1/forecast",
                params={
                    "latitude": lat,
                    "longitude": lon,
                    "current": "temperature_2m,weather_code,wind_speed_10m",
                },
            )
            weather.raise_for_status()
            current = weather.json().get("current", {})
            temp = current.get("temperature_2m")
            wind = current.get("wind_speed_10m")
            return SkillResult(
                response=(
                    f"It's {temp}°C in {resolved} with winds of {wind} km/h."
                    if temp is not None
                    else f"I couldn't fetch weather for {resolved}."
                ),
                data={"city": resolved, "temperature": temp, "wind": wind},
            )

    @staticmethod
    def _extract_city(utterance: str) -> str:
        for pattern in (
            r"\bweather (?:in |for )?(.+)",
            r"\b(?:how'?s|what'?s) the weather (?:in |for )?(.+)",
            r"\btemperature (?:in |for )?(.+)",
        ):
            m = re.search(pattern, utterance, re.IGNORECASE)
            if m and m.group(1):
                return m.group(1).strip(" ?.!")
        return ""


_: Skill = WeatherSkill()
