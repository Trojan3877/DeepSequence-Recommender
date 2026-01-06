import torch
import torch.nn as nn


class TwoTowerModel(nn.Module):
    def __init__(self, num_users, num_items, embed_dim=64):
        super().__init__()

        self.user_embedding = nn.Embedding(num_users, embed_dim)
        self.item_embedding = nn.Embedding(num_items, embed_dim)

        self.user_tower = nn.Sequential(
            nn.Linear(embed_dim, 128),
            nn.ReLU(),
            nn.Linear(128, embed_dim)
        )

        self.item_tower = nn.Sequential(
            nn.Linear(embed_dim, 128),
            nn.ReLU(),
            nn.Linear(128, embed_dim)
        )

    def forward(self, user_ids, item_ids):
        user_vec = self.user_tower(self.user_embedding(user_ids))
        item_vec = self.item_tower(self.item_embedding(item_ids))

        scores = (user_vec * item_vec).sum(dim=1)
        return scores