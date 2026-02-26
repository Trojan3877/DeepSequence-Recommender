from fastapi import FastAPI
import numpy as np

from retrieval.candidate_generator import CandidateGenerator
from models.transformer import TransformerRecommender

app = FastAPI(title="DeepSequence Recommender API")

model = None
candidate_generator = None


@app.on_event("startup")
def load_components():
    global model
    model = TransformerRecommender(
        num_items=10000,
        embedding_dim=64,
        max_sequence_length=50
    )
    model.build()


@app.post("/recommend")
def recommend(sequence: list):
    sequence = np.array(sequence).reshape(1, -1)
    predictions = model.predict(sequence)
    top_items = predictions.argsort()[0][-10:][::-1]
    return {"recommendations": top_items.tolist()}