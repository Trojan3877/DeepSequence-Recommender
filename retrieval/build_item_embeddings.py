import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

EMBEDDING_DIM = 64

def build_item_embeddings(item_df: pd.DataFrame) -> np.ndarray:
    """
    Build dense item embeddings from metadata.
    In production this would come from a deep model.
    """
    enc = LabelEncoder()
    item_ids = enc.fit_transform(item_df["item_id"])

    rng = np.random.default_rng(seed=42)
    embeddings = rng.normal(size=(len(item_ids), EMBEDDING_DIM)).astype("float32")

    np.save("retrieval/item_embeddings.npy", embeddings)
    np.save("retrieval/item_ids.npy", item_ids)

    return embeddings


if __name__ == "__main__":
    items = pd.read_csv("data/items.csv")
    build_item_embeddings(items)