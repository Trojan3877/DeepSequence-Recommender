import time
import numpy as np

class LatencyIsolatedFeatureStore:
    """
    Implements a fast dual-storage retrieval mock pattern 
    optimized for sub-2ms historical state sequence assemblies.
    """
    def __init__(self):
        # Mock in-memory low-latency hash map key storage
        self.redis_in_memory_cache = {
            "user_8271": [102, 405, 12, 994, 58, 230, 41, 88],
            "user_1194": [22, 940, 503, 112, 8],
            "user_4952": [1094, 2390, 44, 12, 853, 901, 33, 442, 129]
        }
        self.vocab_size = 5000
        self.target_sequence_len = 50

    def fetch_user_realtime_sequence(self, user_id: str):
        start_time = time.time()
        
        # Look up rolling click event tokens from the in-memory cache
        raw_sequence = self.redis_in_memory_cache.get(user_id, [])
        
        # Fail-safe padding: align the variable-length history to a fixed input window
        if len(raw_sequence) < self.target_sequence_len:
            pad_size = self.target_sequence_len - len(raw_sequence)
            padded_sequence = [0] * pad_size + raw_sequence
        else:
            padded_sequence = raw_sequence[-self.target_sequence_len:]
            
        retrieval_latency = (time.time() - start_time) * 1000
        return np.array([padded_sequence], dtype=np.int64), retrieval_latency
