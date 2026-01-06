def apply_fairness(items, group_key="provider"):
    """
    Ensures exposure balance across item providers.
    """
    seen = set()
    balanced = []

    for item in items:
        group = item[group_key]
        if group not in seen:
            balanced.append(item)
            seen.add(group)

    # Append remaining items
    for item in items:
        if item not in balanced:
            balanced.append(item)

    return balanced