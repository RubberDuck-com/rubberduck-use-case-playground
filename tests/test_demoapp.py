from demoapp.db.query import Compiler, Query


def test_annotation_select_is_masked_subset():
    q = Query()
    q.annotations = {"a": 1, "b": 2}
    q.set_annotation_mask({"a"})
    assert list(q.annotation_select) == ["a"]


def test_get_order_by_distinguishes_ref_and_annotation():
    q = Query()
    q.annotations = {"hour": "expr"}
    q.set_annotation_mask(set())
    compiler = Compiler(q)
    kind, is_ref = compiler.get_order_by("hour")
    assert is_ref is False
    assert kind == "OrderByAnnotation"
