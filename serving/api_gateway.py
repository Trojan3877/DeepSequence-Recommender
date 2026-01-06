from fastapi import FastAPI
from schemas import RecommendationRequest, RecommendationResponse
from cache import get_cached, set_cached
from inference_pipeline import run_inference

app = FastAPI(title="Recommendation API Gateway")


@app.post("/recommend", response_model=RecommendationResponse)
def recommend(req: RecommendationRequest):
    cache_key = f"user:{req.user_id}"

    cached = get_cached(cache_key)
    if cached:
        return cached

    # Placeholder ranked_items (from Phase 2 output)
    ranked_items = [
        {"item_id": 1, "score": 0.91, "category": "A", "timestamp": 1710000000, "provider": "X"},
        {"item_id": 2, "score": 0.89, "category": "B", "timestamp": 1720000000, "provider": "Y"},
    ]

    final_items = run_inference(
        user_embedding=req.user_embedding,
        ranked_items=ranked_items
    )

    response = {
        "recommendations": [item["item_id"] for item in final_items]
    }

    set_cached(cache_key, response)
    return response