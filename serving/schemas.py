from pydantic import BaseModel
from typing import List


class RecommendationRequest(BaseModel):
    user_id: int
    user_embedding: List[float]


class RecommendationResponse(BaseModel):
    recommendations: List[int]