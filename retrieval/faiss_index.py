import faiss
import numpy as np
from pathlib import Path


class FaissIndex:

    def __init__(self, dimension: int, index_path: str):
        self.dimension = dimension
        self.index_path = Path(index_path)
        self.index = faiss.IndexFlatL2(dimension)

    def build(self, embeddings: np.ndarray):
        if embeddings.shape[1] != self.dimension:
            raise ValueError("Embedding dimension mismatch.")
        self.index.add(embeddings.astype(np.float32))

    def search(self, query_vector: np.ndarray, top_k: int = 10):
        distances, indices = self.index.search(
            query_vector.astype(np.float32), top_k
        )
        return distances, indices

    def save(self):
        faiss.write_index(self.index, str(self.index_path))

    def load(self):
        self.index = faiss.read_index(str(self.index_path))