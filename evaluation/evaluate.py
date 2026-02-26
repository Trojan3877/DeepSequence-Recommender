import numpy as np
from evaluation.metrics import (
    recall_at_k,
    precision_at_k,
    ndcg_at_k,
    hit_rate_at_k
)


def evaluate(y_true, y_pred):
    results = {
        "Recall@10": recall_at_k(y_true, y_pred, k=10),
        "Precision@10": precision_at_k(y_true, y_pred, k=10),
        "NDCG@10": ndcg_at_k(y_true, y_pred, k=10),
        "HitRate@10": hit_rate_at_k(y_true, y_pred, k=10),
    }

    return results