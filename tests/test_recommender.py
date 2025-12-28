from app.train import LSTMRecommender
import torch

def test_forward():
    model = LSTMRecommender(vocab_size=100)
    seq = torch.randint(0, 100, (1,10))
    output = model(seq)
    assert output.shape[-1] == 100
