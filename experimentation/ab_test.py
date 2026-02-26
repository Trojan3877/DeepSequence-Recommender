import random


class ABTestRouter:

    def __init__(self, split_ratio=0.5):
        self.split_ratio = split_ratio

    def route(self, user_id: int):
        random.seed(user_id)
        if random.random() < self.split_ratio:
            return "model_A"
        return "model_B"