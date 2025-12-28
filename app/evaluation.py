import numpy as np

def precision_at_k(preds, truth, k=10):
    return len(set(preds[:k]) & set(truth[:k])) / k

def mean_average_precision(preds, truth, k=10):
    return np.mean([precision_at_k(p, t, k) for p, t in zip(preds, truth)])
