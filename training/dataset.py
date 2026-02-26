import numpy as np
import pandas as pd
from typing import Tuple


class SequenceDataset:
    """
    Converts user-item interaction logs into fixed-length sequences
    for sequence-based recommendation models.
    """

    def __init__(self, max_sequence_length: int):
        self.max_sequence_length = max_sequence_length

    def build_sequences(
        self,
        interactions: pd.DataFrame,
        user_col: str = "user_id",
        item_col: str = "item_id",
        time_col: str = "timestamp"
    ) -> Tuple[np.ndarray, np.ndarray]:

        interactions = interactions.sort_values([user_col, time_col])

        sequences = []
        targets = []

        for user_id, group in interactions.groupby(user_col):
            items = group[item_col].values

            for i in range(1, len(items)):
                seq = items[max(0, i - self.max_sequence_length):i]
                seq = self._pad_sequence(seq)
                sequences.append(seq)
                targets.append(items[i])

        return np.array(sequences), np.array(targets)

    def _pad_sequence(self, sequence):
        padded = np.zeros(self.max_sequence_length)
        padded[-len(sequence):] = sequence
        return padded