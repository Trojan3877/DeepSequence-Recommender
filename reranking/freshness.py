import time

def apply_freshness(items, decay=0.0001):
    """
    Penalizes stale items using exponential decay.
    """
    now = time.time()

    for item in items:
        age = now - item["timestamp"]
        item["score"] *= (2.71828 ** (-decay * age))

    return sorted(items, key=lambda x: x["score"], reverse=True)