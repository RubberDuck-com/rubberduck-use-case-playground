"""Tests-first: parallel write flag (UC-06) — fails until implemented."""
from demoapp.builders.html import StandaloneHTMLBuilder
from demoapp.application import Application


def test_parallel_write_flag_exists():
    app = Application(srcdir=".")
    builder = StandaloneHTMLBuilder(app)
    # Fails on purpose until --parallel-write is implemented (UC-06 tests-first).
    assert getattr(builder, "parallel_write_safe", False) is True
