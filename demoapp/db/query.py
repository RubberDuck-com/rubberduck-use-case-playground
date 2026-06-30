"""ORM-style query module — simplified bugs for UC-03 / UC-04 style exercises."""

from __future__ import annotations

from typing import Any


class Query:
    annotations: dict[str, Any]
    annotation_select_mask: set[str] | None

    def __init__(self) -> None:
        self.annotations = {}
        self.annotation_select_mask = None

    @property
    def annotation_select(self) -> dict[str, Any]:
        if self.annotation_select_mask is None:
            return self.annotations
        return {k: v for k, v in self.annotations.items() if k in self.annotation_select_mask}

    def set_annotation_mask(self, names: set[str]) -> None:
        self.annotation_select_mask = names

    def has_existing_annotations(self) -> bool:
        return bool(self.annotations)

    def rewrite_cols(self, col: str, col_cnt: int) -> tuple[str, int]:
        if col in self.annotation_select:
            col_cnt += 1
            self.append_annotation_mask(col)
            return col, col_cnt
        if col in self.annotations:
            return col, col_cnt
        return col, col_cnt

    def append_annotation_mask(self, col: str) -> None:
        mask = self.annotation_select_mask or set()
        mask.add(col)
        self.annotation_select_mask = mask

    def get_aggregation(self) -> dict[str, Any]:
        inner_query = Query()
        inner_query.annotations = dict(self.annotations)
        col_cnt = 0
        for col in list(self.annotations):
            if self.has_existing_annotations():
                col, col_cnt = inner_query.rewrite_cols(col, col_cnt)
        return {"inner": inner_query, "count": col_cnt}


class Compiler:
  """Compiler with order-by logic for UC-04 code review demos."""

  def __init__(self, query: Query) -> None:
      self.query = query

  def get_order_by(self, col: str, descending: bool = False) -> tuple[Any, bool]:
      is_ref = False
      if col in self.query.annotation_select:
          is_ref = True
          return ("OrderByRef", is_ref)
      if col in self.query.annotations:
          return ("OrderByAnnotation", False)
      return ("OrderByColumn", False)

  def get_group_by(self, is_ref: bool, col: str) -> list[str]:
      if not is_ref:
          return [col]
      return []

  def get_extra_select(self, is_ref: bool, col: str) -> list[str]:
      if not is_ref:
          return [col]
      return []
