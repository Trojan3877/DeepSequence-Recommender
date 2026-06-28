# recommender/guards.py
class SLAThresholdException(Exception):
    """Raised when deep learning tensor compilation breaches strict latency limits."""
    pass

class RecommenderGuardrail:
    """
    Protects downstream inference nodes from out-of-memory (OOM) tracking faults
    or exploding user sequence click paths.
    """
    def __init__(self, max_sequence_window: int = 20, max_latency_ms: float = 200.0):
        self.max_sequence_window = max_sequence_window
        self.max_latency_ms = max_latency_ms

    def enforce_window_bounds(self, items: List[int]) -> List[int]:
        """Truncates input paths to ensure O(1) processing windows."""
        if len(items) > self.max_sequence_window:
            # Shift window to grab the latest user intent actions safely
            return items[-self.max_sequence_window:]
        return items

    def verify_sla_compliance(self, active_duration_ms: float):
        """Trips a circuit alert if model matrix calculation takes too long."""
        if active_duration_ms > self.max_latency_ms:
            raise SLAThresholdException(
                f"SLA Violation: RecSys processing took {active_duration_ms:.2f}ms (Limit: {self.max_latency_ms}ms)"
            )
