import numpy as np


def recall_at_k(y_true, y_pred, k=10):
    """
    y_true: list of true item ids
    y_pred: list of predicted ranked item lists
    """
    recalls = []

    for true_item, pred_items in zip(y_true, y_pred):
        pred_k = pred_items[:k]
        recalls.append(int(true_item in pred_k))

    return np.mean(recalls)


def precision_at_k(y_true, y_pred, k=10):
    precisions = []

    for true_item, pred_items in zip(y_true, y_pred):
        pred_k = pred_items[:k]
        precisions.append(int(true_item in pred_k) / k)

    return np.mean(precisions)


def ndcg_at_k(y_true, y_pred, k=10):
    """
    Normalized Discounted Cumulative Gain
    """
    ndcgs = []

    for true_item, pred_items in zip(y_true, y_pred):
        dcg = 0.0
        for i, item in enumerate(pred_items[:k]):
            if item == true_item:
                dcg = 1 / np.log2(i + 2)
                break

        idcg = 1.0  # Only 1 relevant item
        ndcgs.append(dcg / idcg)

    return np.mean(ndcgs)


def hit_rate_at_k(y_true, y_pred, k=10):
    hits = []

    for true_item, pred_items in zip(y_true, y_pred):
        hits.append(int(true_item in pred_items[:k]))

    return np.mean(hits)