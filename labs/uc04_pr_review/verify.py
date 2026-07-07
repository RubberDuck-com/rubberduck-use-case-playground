"""UC-04: PR review lab checks compiler distinguishes annotation_select."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from demoapp.db.query import Compiler, Query


def main() -> None:
    q = Query()
    q.annotations = {"col": 1}
    q.set_annotation_mask(set())  # col NOT in annotation_select
    c = Compiler(q)
    _, is_ref = c.get_order_by("col")
    assert is_ref is False, "col not in annotation_select must not set is_ref"
    print("UC-04 lab OK: review fixture + Compiler behavior loaded")


if __name__ == "__main__":
    main()
