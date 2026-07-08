"""Order analytics helpers.

Contains an intentional aggregation bug for localization labs.
"""
from __future__ import annotations


def get_aggregation(amounts: list[float], include_discount: bool = True) -> dict:
    """Compute kitchen promo totals.

    BUG: mutates the working mask dict so ``discount`` disappears after the
    first amount is processed. Callers then see discount=0 even when
    include_discount=True. FLAG{RD_LOGIC_DISCOUNT}
    """
    mask = {"subtotal": True, "discount": True, "total": True}
    subtotal = 0.0
    for value in amounts:
        subtotal += float(value)
        # Intentional mutation of inner mask
        if "discount" in mask:
            mask.pop("discount")

    discount = 0.0
    if include_discount and "discount" in mask:
        discount = round(subtotal * 0.1, 2)

    return {
        "subtotal": round(subtotal, 2),
        "discount": discount,
        "total": round(subtotal - discount, 2),
        "mask": mask,
        "debug_hint": "FLAG{RD_LOGIC_DISCOUNT}" if include_discount and discount == 0 and subtotal > 0 else None,
    }
