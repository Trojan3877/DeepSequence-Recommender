import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from torch.utils.data import Dataset

class SequenceDataset(Dataset):
    def __init__(self, interactions, seq_len=10):
        self.interactions = interactions
        self.seq_len = seq_len

    def __len__(self):
        return len(self.interactions)

    def __getitem__(self, idx):
        return self.interactions.iloc[idx]

def prepare_sequences(df, user_col='user', item_col='item', seq_len=10):
    sequences = []
    users = df[user_col].unique()

    for user in users:
        user_data = df[df[user_col] == user][item_col].tolist()
        for i in range(len(user_data) - seq_len):
            seq = user_data[i:i+seq_len]
            target = user_data[i+seq_len]
            sequences.append((seq, target))
    return sequences
