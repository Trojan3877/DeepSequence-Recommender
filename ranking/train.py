import torch
from torch.utils.data import DataLoader
from two_tower_model import TwoTowerModel
from dataset import RankingDataset

device = "cuda" if torch.cuda.is_available() else "cpu"

interactions = [(0, 10), (1, 20), (2, 30)]  # placeholder
num_users = 1000
num_items = 5000

dataset = RankingDataset(interactions, num_items)
loader = DataLoader(dataset, batch_size=32, shuffle=True)

model = TwoTowerModel(num_users, num_items).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
loss_fn = torch.nn.BCEWithLogitsLoss()

for epoch in range(5):
    for batch in loader:
        users = batch["user"].to(device)
        pos_items = batch["pos_item"].to(device)
        neg_items = batch["neg_item"].to(device)

        pos_scores = model(users, pos_items)
        neg_scores = model(users, neg_items)

        labels = torch.cat([
            torch.ones_like(pos_scores),
            torch.zeros_like(neg_scores)
        ])

        loss = loss_fn(
            torch.cat([pos_scores, neg_scores]),
            labels
        )

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch} Loss: {loss.item():.4f}")