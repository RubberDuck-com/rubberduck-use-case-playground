# UC-04 sample PR diff (order-by simplification)

Review this change in `demoapp/db/query.py` / `Compiler.get_order_by`.

## Before

```python
if col in self.query.annotation_select:
    is_ref = True
    return ("OrderByRef", is_ref)
if col in self.query.annotations:
    return ("OrderByAnnotation", False)
```

## After (proposed — intentionally risky)

```python
if col in self.query.annotations:
    is_ref = True
    return ("OrderByRef", is_ref)
```

Ask RubberDuck to verify whether `annotation_select` is always a subset of `annotations` and trace `is_ref` to `get_group_by` and `get_extra_select`.
