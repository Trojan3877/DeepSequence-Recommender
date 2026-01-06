import faiss
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

EMBEDDING_DIM = 64
TOP_K = 200

app = FastAPI(title="ANN Retrieval Service")

index = faiss.read_index("retrieval/faiss.index")
item_ids = np.load("retrieval/item_ids.npy")


class Query(BaseModel):
    user_embedding: list[float]


@app.post("/retrieve")
def retrieve_candidates(query: Query):
    user_vector = np.array(query.user_embedding, dtype="float32").reshape(1, -1)

    distances, indices = index.search(user_vector, TOP_K)
    candidates = item_ids[indices[0]].tolist()

    return {
        "candidates": candidates,
        "count": len(candidates)
    }