import random

def assign_variant(user_id: int, ratio=0.1):
    """
    Assigns user to experiment group.
    """
    return "experiment" if random.random() < ratio else "control"