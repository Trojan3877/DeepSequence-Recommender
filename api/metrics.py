from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "api_requests_total",
    "Total number of API requests"
)

REQUEST_LATENCY = Histogram(
    "api_request_latency_seconds",
    "Latency of API requests"
)

from prometheus_client import start_http_server
from api.metrics import REQUEST_COUNT, REQUEST_LATENCY
import time

start_http_server(9000)

@app.post("/recommend")
def recommend(sequence: list):
    REQUEST_COUNT.inc()

    start = time.time()
    sequence = np.array(sequence).reshape(1, -1)
    predictions = model.predict(sequence)
    latency = time.time() - start

    REQUEST_LATENCY.observe(latency)

    top_items = predictions.argsort()[0][-10:][::-1]
    return {"recommendations": top_items.tolist()}

http://localhost:9000/metrics