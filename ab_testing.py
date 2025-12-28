import random

def assign_variant(user_id):
    return "treatment" if hash(user_id) % 2 == 0 else "control"
