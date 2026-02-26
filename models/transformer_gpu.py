import torch
import torch.nn as nn


class TransformerRecommender(nn.Module):

    def __init__(self, num_items, embedding_dim=64, seq_len=50):
        super().__init__()

        self.embedding = nn.Embedding(num_items + 1, embedding_dim)
        self.transformer = nn.TransformerEncoder(
            nn.TransformerEncoderLayer(
                d_model=embedding_dim,
                nhead=4,
                batch_first=True
            ),
            num_layers=2
        )

        self.fc = nn.Linear(embedding_dim, num_items)

    def forward(self, x):
        x = self.embedding(x)
        x = self.transformer(x)
        x = x.mean(dim=1)
        return self.fc(x)


def load_model(model_path, device):
    model = TransformerRecommender(
        num_items=10000,
        embedding_dim=64,
        seq_len=50
    )
    model.load_state_dict(torch.load(model_path, map_location=device))
    model.to(device)
    model.eval()
    return model