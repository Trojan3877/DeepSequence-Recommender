from experimentation.ab_test import ABTestRouter

router = ABTestRouter(split_ratio=0.5)

@app.post("/recommend/{user_id}")
def recommend(user_id: int, sequence: list):

    model_group = router.route(user_id)

    if model_group == "model_A":
        results = inference_pipeline_model_a(sequence)
    else:
        results = inference_pipeline_model_b(sequence)

    return {
        "model_served": model_group,
        "recommendations": results
    }