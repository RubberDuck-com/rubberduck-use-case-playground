import inspect
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from demoapp.builders.html import StandaloneHTMLBuilder


def main() -> None:
    src = inspect.getsource(StandaloneHTMLBuilder.render_partial)
    assert "fragment" in src
    print("UC-10 lab OK: render_partial is", len(src.splitlines()), "lines — quick-check target")


if __name__ == "__main__":
    main()
