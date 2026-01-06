import numpy as np


def detect_drift(reference, current, threshold=0.1):
    ref_mean = np.mean(reference)
    cur_mean = np.mean(current)

    drift = abs(ref_mean - cur_mean) / ref_mean
    return drift > threshold