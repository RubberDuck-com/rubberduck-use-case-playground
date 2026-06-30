"""CLI entry points — trace with call_chain for UC-01."""

from __future__ import annotations

import argparse
import sys

from demoapp.application import Application
from demoapp.config import Config


def handle_exception(exc: BaseException) -> int:
    print(f"build failed: {exc}", file=sys.stderr)
    return 1


def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="demoapp-build")
    parser.add_argument("srcdir")
    parser.add_argument("-c", "--config", default=None)
    return parser


def make_main(argv: list[str] | None = None) -> argparse.Namespace:
    return get_parser().parse_args(argv)


def build_main(argv: list[str] | None = None) -> int:
    args = make_main(argv)
    config = Config(args.config) if args.config else Config()
    app = Application(args.srcdir, config)
    try:
        app.build()
    except Exception as exc:  # noqa: BLE001
        return handle_exception(exc)
    return 0


def main(argv: list[str] | None = None) -> int:
    return build_main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
