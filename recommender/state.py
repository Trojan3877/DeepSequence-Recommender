# recommender/state.py
from pydantic import BaseModel, Field
from typing import List, Optional

class SessionState(BaseModel):
    """
    The immutable token tracking contract passed across the inference pipeline.
    Enforces structural context bounds on raw clickstream sequences.
    """
    session_id: str
    raw_item_history: List[int] = Field(default_factory=list)
    processed_tensor_input: Optional[List[float]] = None
    top_k_recommendations: List[int] = Field(default_factory=list)
    prediction_confidence: List[float] = Field(default_factory=list)
    
    # Operational Observability
    sequence_length: int = 0
    inference_latency_ms: float = 0.0
    fallback_triggered: bool = False
    execution_trace: List[str] = Field(default_factory=list)

    def log_trace(self, message: str) -> "SessionState":
        return self.model_copy(update={"execution_steps": list(self.execution_trace) + [message]})
