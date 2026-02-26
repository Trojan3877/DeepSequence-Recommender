import numpy as np


class DriftDetector:

    def detect(self, baseline_distribution, current_distribution):
        return np.abs(
            baseline_distribution.mean() - current_distribution.mean()
        )