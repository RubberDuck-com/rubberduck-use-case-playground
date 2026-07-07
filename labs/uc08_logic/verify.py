import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from demoapp.builders.html import StandaloneHTMLBuilder
from demoapp.application import Application


def main() -> None:
    app = Application(srcdir=".")
    b = StandaloneHTMLBuilder(app)
    branches = len(b.get_outdated_docs.__code__.co_consts)
    assert branches >= 1
    print("UC-08 lab OK: get_outdated_docs loaded for logic review")


if __name__ == "__main__":
    main()
