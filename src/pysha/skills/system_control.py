"""Cross-platform system control — launch and close applications."""

from __future__ import annotations

import asyncio
import re
import shutil
import sys

from pysha.skills.base import Skill, SkillContext, SkillResult

# Friendly aliases → executable name (looked up via ``shutil.which``).
_APP_ALIASES = {
    "calculator": {"win32": "calc.exe", "darwin": "Calculator.app", "linux": "gnome-calculator"},
    "notepad": {"win32": "notepad.exe", "darwin": "TextEdit.app", "linux": "gedit"},
    "browser": {"win32": "chrome.exe", "darwin": "Safari.app", "linux": "xdg-open"},
    "terminal": {"win32": "cmd.exe", "darwin": "Terminal.app", "linux": "x-terminal-emulator"},
    "code": {"win32": "code.exe", "darwin": "code", "linux": "code"},
}


class SystemControlSkill:
    name = "system_control"
    description = "Launches, closes, or queries desktop applications on the host."
    triggers = [
        r"\b(?:open|launch|start|run)\s+(.+)",
        r"\b(?:close|quit|kill|stop)\s+(.+)",
    ]

    async def handle(self, ctx: SkillContext) -> SkillResult:
        utt = ctx.utterance.lower()
        open_m = re.search(r"\b(?:open|launch|start|run)\s+(.+)", utt)
        close_m = re.search(r"\b(?:close|quit|kill|stop)\s+(.+)", utt)
        if open_m:
            return await self._open(open_m.group(1).strip(" ?.!"))
        if close_m:
            return await self._close(close_m.group(1).strip(" ?.!"))
        return SkillResult(response="I'm not sure what you want me to control.", handled=False)

    async def _open(self, app: str) -> SkillResult:
        exe = self._resolve(app)
        if not exe:
            return SkillResult(response=f"I couldn't find {app} on this system.")
        try:
            if sys.platform == "darwin" and exe.endswith(".app"):
                await asyncio.create_subprocess_exec("open", "-a", exe[:-4])
            else:
                await asyncio.create_subprocess_exec(exe)
            return SkillResult(response=f"Opening {app}.")
        except Exception as exc:
            return SkillResult(response=f"Failed to open {app}: {exc}")

    async def _close(self, app: str) -> SkillResult:
        try:
            import psutil  # type: ignore[import-not-found]
        except ImportError:
            return SkillResult(
                response="Install the system extra: pip install 'pysha[skills-system]'.",
                handled=True,
            )
        closed = 0
        for proc in psutil.process_iter(["name"]):
            if app.lower() in (proc.info.get("name") or "").lower():
                try:
                    proc.terminate()
                    closed += 1
                except psutil.Error:
                    continue
        if closed:
            return SkillResult(response=f"Closed {closed} {app} process(es).")
        return SkillResult(response=f"No running {app} process found.")

    @staticmethod
    def _resolve(app: str) -> str | None:
        if app in _APP_ALIASES:
            candidate = _APP_ALIASES[app].get(sys.platform)
            if candidate and (shutil.which(candidate) or candidate.endswith(".app")):
                return candidate
        return shutil.which(app)


_: Skill = SystemControlSkill()
