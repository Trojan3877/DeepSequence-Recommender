from fastapi import FastAPI
from recommender import prepare_sequences
import torch

app = FastAPI()

@app.post("/predict")
def predict(user_sequence: list[int]):
    model = torch.load("model.pth")
    seq_tensor = torch.tensor(user_sequence).long().unsqueeze(0)
    output = model(seq_tensor)
    preds = output.detach().numpy().argsort()[::-1]
    return {"predictions": preds.tolist()[:10]}

