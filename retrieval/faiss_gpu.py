import faiss
import numpy as np


class FaissGPU:

    def __init__(self, dimension):
        self.res = faiss.StandardGpuResources()
        cpu_index = faiss.IndexFlatL2(dimension)
        self.index = faiss.index_cpu_to_gpu(self.res, 0, cpu_index)

    def build(self, embeddings):
        self.index.add(embeddings.astype(np.float32))

    def search(self, query, top_k):
        return self.index.search(query.astype(np.float32), top_k)