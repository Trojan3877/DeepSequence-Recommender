import torch
from torch.utils.data import Dataset
import random


class RankingDataset(Dataset):
    def __init__(self, interactions, num_items):
        self.interactions = interactions
        self.num_items = num_items

    def __len__(self):
        return len(self.interactions)

    def __getitem__(self, idx):
        user, pos_item = self.interactions[idx]
        neg_item = random.randint(0, self.num_items - 1)

        return {
            "user": torch.tensor(user),
            "pos_item": torch.tensor(pos_item),
            "neg_item": torch.tensor(neg_item)
        }