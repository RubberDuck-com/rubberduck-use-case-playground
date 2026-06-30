"""Application core — entry point for UC-01 / UC-08 / UC-10 demos."""

from __future__ import annotations

import os
from typing import Any

from demoapp.config import Config


class BuildInfo:
    """Tracks build metadata for staleness checks (UC-08)."""

    def __init__(self, config: Config, tags: list[str], builders: list[str]) -> None:
        self.config_hash = hash(frozenset(config.config_values.items()))
        self.tags_hash = hash(tuple(tags))
        self.builders = builders

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BuildInfo):
            return False
        return self.config_hash == other.config_hash and self.tags_hash == other.tags_hash

    @classmethod
    def load(cls, path: str) -> "BuildInfo":
        return cls(Config(), [], ["html"])

    @classmethod
    def create(cls, config: Config, tags: list[str]) -> "BuildInfo":
        return cls(config, tags, ["html"])


class Application:
    """Main application object."""

    def __init__(self, srcdir: str, config: Config | None = None) -> None:
        self.srcdir = srcdir
        self.config = config or Config()
        self.env: dict[str, Any] = {"all_docs": {}}
        self.tags: list[str] = []
        self.builder = None

    def build(self, filenames: list[str] | None = None) -> None:
        from demoapp.builders.html import StandaloneHTMLBuilder

        self.builder = StandaloneHTMLBuilder(self)
        self.builder.build(filenames or [])

    def emit(self, event: str, *args: Any) -> None:
        pass
