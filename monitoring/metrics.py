from prometheus_client import Counter

prediction_requests = Counter(
    "recommender_requests_total",
    "Total prediction requests"
)
