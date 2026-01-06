import torch
import torch.nn as nn


class TransformerRanker(nn.Module):
    def __init__(self, embed_dim=64, n_heads=4, n_layers=2):
        super().__init__()

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embed_dim,
            nhead=n_heads,
            batch_first=True
        )
        self.encoder = nn.TransformerEncoder(encoder_layer, n_layers)
        self.fc = nn.Linear(embed_dim, 1)

    def forward(self, sequence_embeddings):
        encoded = self.encoder(sequence_embeddings)
        pooled = encoded.mean(dim=1)
        return self.fc(pooled).squeeze()