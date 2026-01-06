from diversity import apply_diversity
from freshness import apply_freshness
from fairness import apply_fairness
from constraints import apply_constraints


def rerank(items, blocked_items=None):
    """
    Applies multi-objective re-ranking pipeline.
    """
    items = apply_constraints(items, blocked_items)
    items = apply_freshness(items)
    items = apply_diversity(items)
    items = apply_fairness(items)

    return items