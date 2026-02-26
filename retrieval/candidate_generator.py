import numpy as np
from retrieval.faiss_index import FaissIndex


class CandidateGenerator:

    def __init__(self, index: FaissIndex):
        self.index = index

    def generate(self, user_embedding: np.ndarray, top_k: int = 50):
        _, indices = self.index.search(user_embedding, top_k)
        return indices[0]