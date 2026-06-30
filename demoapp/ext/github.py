"""External link roles — pattern template for UC-07 codegen."""

from __future__ import annotations

from typing import Callable


def make_link_role(base_url: str, prefix: str = "") -> Callable[[str, str], str]:
    def role(name: str, rawtext: str) -> str:
        slug = rawtext.strip()
        return f'<a href="{base_url}/{prefix}{slug}">{slug}</a>'

    return role


def github_role(name: str, rawtext: str) -> str:
    return make_link_role("https://github.com/issues", "")(name, rawtext)
