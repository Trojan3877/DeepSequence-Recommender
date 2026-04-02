"""Data pre-processing utilities for sequence recommendation."""

from __future__ import annotations

from typing import Dict, List, Optional

import torch


class SequenceProcessor:
    """Encode raw item interaction histories into padded tensors."""

    def __init__(self, max_length: int = 50) -> None:
        self.max_length = max_length
        self._item2idx: Dict[str, int] = {}
        self._idx2item: Dict[int, str] = {}
        self._next_idx: int = 1  # 0 reserved for padding

    # ------------------------------------------------------------------
    # Vocabulary management
    # ------------------------------------------------------------------

    def fit(self, sequences: List[List[str]]) -> "SequenceProcessor":
        """Build item vocabulary from a list of interaction sequences."""
        for seq in sequences:
            for item in seq:
                if item not in self._item2idx:
                    self._item2idx[item] = self._next_idx
                    self._idx2item[self._next_idx] = item
                    self._next_idx += 1
        return self

    @property
    def vocab_size(self) -> int:
        """Number of known items (excluding padding index 0)."""
        return len(self._item2idx)

    def item_to_idx(self, item: str) -> int:
        """Return numeric index for an item; 0 for unknown items."""
        return self._item2idx.get(item, 0)

    def idx_to_item(self, idx: int) -> Optional[str]:
        """Return item identifier for a numeric index."""
        return self._idx2item.get(idx)

    # ------------------------------------------------------------------
    # Encoding
    # ------------------------------------------------------------------

    def encode(self, sequence: List[str]) -> List[int]:
        """Convert a list of item IDs to a list of numeric indices."""
        return [self.item_to_idx(item) for item in sequence]

    def pad_sequence(self, indices: List[int]) -> List[int]:
        """Truncate to max_length and left-pad with zeros."""
        indices = indices[-self.max_length :]
        padded = [0] * (self.max_length - len(indices)) + indices
        return padded

    def to_tensor(self, sequence: List[str]) -> torch.Tensor:
        """Encode and pad a single sequence, returning shape ``(1, max_length)``."""
        indices = self.encode(sequence)
        padded = self.pad_sequence(indices)
        return torch.tensor([padded], dtype=torch.long)

    def decode_recommendations(self, indices: List[int]) -> List[Optional[str]]:
        """Map numeric recommendation indices back to item identifiers."""
        return [self.idx_to_item(idx) for idx in indices]
