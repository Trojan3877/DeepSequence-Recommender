import numpy as np
from retrieval.faiss_index import FaissIndex


class VectorStore:

    def __init__(self, index_path: str, embedding_dim: int):
        self.index = FaissIndex(dimension=embedding_dim, index_path=index_path)
        self.index.load()

    def retrieve(self, user_embedding: np.ndarray, top_k: int = 100):
        distances, indices = self.index.search(user_embedding, top_k)
        return indices[0]