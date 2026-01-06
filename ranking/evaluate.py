import numpy as np


def ndcg_at_k(scores, k=10):
    scores = np.array(scores)
    order = np.argsort(scores)[::-1][:k]
    gains = 2 ** scores[order] - 1
    discounts = np.log2(np.arange(len(gains)) + 2)
    return np.sum(gains / discounts)


def recall_at_k(relevant, recommended, k=10):
    return len(set(relevant) & set(recommended[:k])) / len(relevant)