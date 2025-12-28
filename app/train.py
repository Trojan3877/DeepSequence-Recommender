import mlflow
from recommender import prepare_sequences, SequenceDataset
import torch
from torch import nn
from torch.utils.data import DataLoader

class LSTMRecommender(nn.Module):
    def __init__(self, vocab_size, embed_dim=128, hidden_dim=256):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, batch_first=True)
        self.output = nn.Linear(hidden_dim, vocab_size)

    def forward(self, x):
        x = self.embedding(x)
        out, _ = self.lstm(x)
        return self.output(out[:, -1])

def train_model(sequences, vocab_size, epochs=10):
    dataset = SequenceDataset(sequences)
    loader = DataLoader(dataset, batch_size=64, shuffle=True)

    model = LSTMRecommender(vocab_size)
    loss_fn = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

    mlflow.set_experiment("DeepSequence_Recommender")

    with mlflow.start_run():
        mlflow.log_param("vocab_size", vocab_size)

        for epoch in range(epochs):
            total_loss = 0
            for seq, target in loader:
                optimizer.zero_grad()
                seq_tensor = torch.tensor(seq).long()
                target_tensor = torch.tensor(target).long()

                output = model(seq_tensor)
                loss = loss_fn(output, target_tensor)
                loss.backward()
                optimizer.step()
                total_loss += loss.item()

            mlflow.log_metric("loss", total_loss, step=epoch)
            print(f"Epoch {epoch} | Loss: {total_loss:.4f}")

    return model
