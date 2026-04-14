"""Plugin discovery via Python entry-point groups.

This is the mechanism that lets PYSHA remain **open-source at its core** while
supporting **closed-source engines**.  Any package — proprietary or otherwise —
can register an engine or skill by declaring an entry-point in its own
``pyproject.toml``.  PYSHA discovers it at runtime without any imports or
hard-coded references.

Entry-point groups
------------------
- ``pysha.engines.stt``  — Speech-to-Text engines
- ``pysha.engines.tts``  — Text-to-Speech engines
- ``pysha.engines.llm``  — Large Language Model engines
- ``pysha.skills``       — Assistant skills / plugins
"""

from __future__ import annotations

import importlib.metadata
from typing import Any

import structlog

logger = structlog.get_logger(__name__)


class PluginLoader:
    """Discovers and instantiates plugins from entry-point groups."""

    @staticmethod
    def list_plugins(group: str) -> dict[str, importlib.metadata.EntryPoint]:
        """Return a ``{name: entry_point}`` mapping for the given group."""
        eps = importlib.metadata.entry_points()
        # Python 3.12+ returns a SelectableGroups; 3.9-3.11 returns a dict.
        selected = eps.select(group=group) if hasattr(eps, "select") else eps.get(group, [])
        return {ep.name: ep for ep in selected}

    @staticmethod
    def load(group: str, name: str, **kwargs: Any) -> Any:
        """Load a single plugin by *group* and *name*, passing ``kwargs`` to its constructor."""
        plugins = PluginLoader.list_plugins(group)
        if name not in plugins:
            available = ", ".join(sorted(plugins)) or "(none)"
            raise ValueError(
                f"No plugin '{name}' in group '{group}'. Available: {available}"
            )
        ep = plugins[name]
        cls = ep.load()
        logger.info("plugin.loaded", group=group, name=name, cls=cls.__qualname__)
        return cls(**kwargs)

    @staticmethod
    def load_all(group: str, **kwargs: Any) -> dict[str, Any]:
        """Load every plugin in *group*, returning ``{name: instance}``."""
        result: dict[str, Any] = {}
        for name, ep in PluginLoader.list_plugins(group).items():
            try:
                cls = ep.load()
                result[name] = cls(**kwargs)
                logger.info("plugin.loaded", group=group, name=name)
            except Exception:
                logger.warning("plugin.load_failed", group=group, name=name, exc_info=True)
        return result
