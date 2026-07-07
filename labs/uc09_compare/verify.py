import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from demoapp.builders.html import Epub3Builder, StandaloneHTMLBuilder
from demoapp.application import Application


def main() -> None:
    app = Application(srcdir=".")
    html = StandaloneHTMLBuilder(app)
    epub = Epub3Builder(app)
    html.prepare_writing(["index"])
    epub.prepare_writing(["index"])
    extra = set(epub.globalcontext) - set(html.globalcontext)
    assert "theme_writing_mode" in extra
    print("UC-09 lab OK: Epub3 adds keys:", ", ".join(sorted(extra)))


if __name__ == "__main__":
    main()
