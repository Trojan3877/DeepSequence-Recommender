from prometheus_client import Counter, Histogram, Gauge

REQUEST_COUNT = Counter("api_requests_total", "Total API Requests")
REQUEST_LATENCY = Histogram("api_latency_seconds", "API Latency")
ACTIVE_REQUESTS = Gauge("active_requests", "Active Requests")

@app.post("/recommend")
def recommend(sequence: list):

    ACTIVE_REQUESTS.inc()
    REQUEST_COUNT.inc()

    start = time.time()

    try:
        sequence = np.array(sequence).reshape(1, -1)
        results = inference_pipeline(sequence)
    finally:
        latency = time.time() - start
        REQUEST_LATENCY.observe(latency)
        ACTIVE_REQUESTS.dec()

    return {"recommendations": results}