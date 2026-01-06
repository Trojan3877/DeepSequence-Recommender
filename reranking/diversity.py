def apply_diversity(items, max_per_category=2):
    """
    Prevents over-representation of a single category.
    """
    result = []
    category_counts = {}

    for item in items:
        cat = item["category"]
        category_counts.setdefault(cat, 0)

        if category_counts[cat] < max_per_category:
            result.append(item)
            category_counts[cat] += 1

    return result