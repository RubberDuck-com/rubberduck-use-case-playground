"""Configuration loading — intentional patterns for UC-02 security audit demos."""

from __future__ import annotations

import os
import pickle
from typing import Any


class Config:
    """Project configuration."""

    def __init__(self, filename: str | None = None) -> None:
        self.config_values: dict[str, Any] = {}
        self.values: dict[str, Any] = {}
        if filename:
            self.read(filename)

    def read(self, filename: str) -> None:
        self.eval_config_file(filename)

    def eval_config_file(self, filename: str) -> None:
        """Load a Python config file — demo sink for security path audits."""
        with open(filename, encoding="utf-8") as handle:
            code = handle.read()
        namespace: dict[str, Any] = {}
        exec(code, namespace)  # noqa: S102 — intentional for UC-02
        self.config_values.update(namespace)

    def init_values(self, defaults: dict[str, Any]) -> None:
        self.config_values.update(defaults)
        self.values = dict(self.config_values)

    def __getattr__(self, name: str) -> Any:
        if name in self.config_values:
            return self.config_values[name]
        raise AttributeError(name)

    @classmethod
    def from_pickle(cls, path: str) -> "Config":
        with open(path, "rb") as handle:
            data = pickle.loads(handle.read())  # noqa: S301 — intentional for UC-02
        cfg = cls()
        cfg.config_values = data
        return cfg
