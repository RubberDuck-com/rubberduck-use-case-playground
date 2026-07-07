"""Actually RUN each use case against the real demoapp code.

Usage: python scripts/demo.py <uc>   (uc = 01..10)

Each demo executes real demoapp code and prints tangible output, so you can
see the actual behavior (including the intentional bugs) before you run
RubberDuck on the same code.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def demo_01() -> None:
    """UC-01 Understand Your Code — build real HTML output."""
    from demoapp.application import Application
    from demoapp.config import Config

    srcdir = ROOT / "sampledocs"
    cfg = Config()
    cfg.init_values({"project": "DemoApp Docs", "version": "0.1.0"})
    app = Application(str(srcdir), cfg)
    app.build(["index"])
    outfile = srcdir / "_build" / "index.html"
    print(f"Entry point: demoapp.cmd.build:main -> Application.build")
    print(f"Built HTML : {outfile}")
    print("-" * 50)
    print(outfile.read_text(encoding="utf-8"))


def demo_02() -> None:
    """UC-02 Codebase Audit — run the vulnerable endpoints in-process."""
    from demoapp.api import server

    injected = "test' OR '1'='1"
    print("Calling search() with a SQL-injection payload:")
    print("  input:", injected)
    print("  built SQL:", server.search(injected)["sql"])
    print()
    print("Sinks to find with RubberDuck UC-02:")
    print("  - demoapp/api/server.py: SQL string built from user input")
    print("  - demoapp/config.py: exec() in eval_config_file, pickle in from_pickle")


def demo_03() -> None:
    """UC-03 Localize and Fix Bugs — run the buggy ORM aggregation live."""
    from demoapp.db.query import Query

    q = Query()
    q.annotations = {"total": "SUM(amount)", "name": "author"}
    result = q.get_aggregation()
    print("annotations           :", q.annotations)
    print("aggregation count     :", result["count"])
    print("inner mask (mutated)  :", result["inner"].annotation_select_mask)
    print()
    print("Bug: get_aggregation mutates the inner query's annotation mask and")
    print("counts only masked columns - RubberDuck UC-03 localizes this in query.py.")


def demo_04() -> None:
    """UC-04 Code Review — run the order-by / group-by compiler logic."""
    from demoapp.db.query import Compiler, Query

    q = Query()
    q.annotations = {"total": "SUM(amount)"}
    q.set_annotation_mask({"total"})
    compiler = Compiler(q)
    order, is_ref = compiler.get_order_by("total")
    print("get_order_by('total') :", (order, is_ref))
    print("get_group_by          :", compiler.get_group_by(is_ref, "total"))
    print("get_extra_select      :", compiler.get_extra_select(is_ref, "total"))
    print()
    print("Review question: when is_ref is True the column is dropped from GROUP BY.")


def demo_05() -> None:
    """UC-05 Change Impact — show the config symbol consumers depend on."""
    from demoapp.config import Config

    cfg = Config()
    cfg.init_values({"project": "demo", "version": "0.1.0"})
    print("Config.config_values :", cfg.config_values)
    print("Config.values mirror :", cfg.values)
    print()
    print("Renaming config_values -> values affects every reader; UC-05 maps them.")


def demo_06() -> None:
    """UC-06 Plan a New Feature — show current (serial) write behavior."""
    from demoapp.builders.html import StandaloneHTMLBuilder

    print("parallel_read_safe  :", StandaloneHTMLBuilder.parallel_read_safe)
    print("parallel_write_safe :", StandaloneHTMLBuilder.parallel_write_safe)
    print()
    print("Feature to plan (UC-06): add --parallel-write. Not implemented yet.")


def demo_07() -> None:
    """UC-07 Generate Code — show existing github role and the missing gitlab one."""
    from demoapp.ext import github

    print("github_role('gh', '123') :", github.github_role("gh", "123"))
    print("gitlab_role implemented  :", hasattr(github, "gitlab_role"))
    print()
    print("CodeGen target (UC-07): add gitlab_role mirroring github_role.")


def demo_08() -> None:
    """UC-08 Check Code Logic — run the staleness logic."""
    from demoapp.application import Application
    from demoapp.builders.html import StandaloneHTMLBuilder

    app = Application(str(ROOT / "sampledocs"))
    app.env["all_docs"] = {"index": 1}
    builder = StandaloneHTMLBuilder(app)
    print("get_outdated_docs() :", builder.get_outdated_docs())
    print()
    print("UC-08 asks: does this correctly detect outdated docs? Note the branches.")


def demo_09() -> None:
    """UC-09 Compare Versions — run HTML vs Epub3 prepare_writing."""
    from demoapp.application import Application
    from demoapp.builders.html import Epub3Builder, StandaloneHTMLBuilder
    from demoapp.config import Config

    cfg = Config()
    cfg.init_values({"project": "demo", "epub_writing_mode": "vertical"})
    app = Application("srcdir", cfg)
    html = StandaloneHTMLBuilder(app)
    html.prepare_writing(["index"])
    epub = Epub3Builder(app)
    epub.prepare_writing(["index"])
    print("HTML  context :", html.globalcontext)
    print("Epub3 context :", epub.globalcontext)
    print()
    print("UC-09 compares the two: Epub3 adds writing-mode / meta-charset keys.")


def demo_10() -> None:
    """UC-10 Quick Check — run render_partial both ways."""
    from demoapp.application import Application
    from demoapp.builders.html import StandaloneHTMLBuilder

    builder = StandaloneHTMLBuilder(Application("srcdir"))
    print("render_partial({'text': 'Hello'}) :", builder.render_partial({"text": "Hello"}))
    print("render_partial(None)              :", builder.render_partial(None))
    print()
    print("UC-10 quick question: what does render_partial do and who calls it?")


DEMOS = {
    "01": demo_01,
    "02": demo_02,
    "03": demo_03,
    "04": demo_04,
    "05": demo_05,
    "06": demo_06,
    "07": demo_07,
    "08": demo_08,
    "09": demo_09,
    "10": demo_10,
}


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if not args:
        print("Usage: python scripts/demo.py <uc 01..10>", file=sys.stderr)
        return 1
    uc = args[0].zfill(2)
    demo = DEMOS.get(uc)
    if not demo:
        print(f"Unknown UC: {uc}", file=sys.stderr)
        return 1
    print("=" * 60)
    print(f"RUN UC-{uc}: executing real demoapp code")
    print("=" * 60)
    demo()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
