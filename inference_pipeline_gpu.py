import torch
import numpy as np
from models.transformer_gpu import load_model


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = load_model("model.pt", device)


def run_inference(sequence):

    sequence = torch.tensor(sequence).long().unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(sequence)

    scores = outputs.cpu().numpy()[0]
    top_items = np.argsort(scores)[-10:][::-1]

    return top_items.tolist()