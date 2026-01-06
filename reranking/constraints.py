def apply_constraints(items, blocked_items=None):
    """
    Removes items that violate business or legal rules.
    """
    if not blocked_items:
        return items

    return [
        item for item in items
        if item["item_id"] not in blocked_items
    ]