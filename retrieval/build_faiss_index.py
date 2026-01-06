import faiss
import numpy as np

EMBEDDING_DIM = 64
INDEX_PATH = "retrieval/faiss.index"

def build_index():
    embeddings = np.load("retrieval/item_embeddings.npy")

    index = faiss.IndexHNSWFlat(EMBEDDING_DIM, 32)
    index.hnsw.efConstruction = 200

    index.add(embeddings)
    faiss.write_index(index, INDEX_PATH)

    print(f"FAISS index built with {index.ntotal} vectors")


if __name__ == "__main__":
    build_index()