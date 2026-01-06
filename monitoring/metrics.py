from prometheus_client import Counter, Histogram

REQUEST_COUNT = Counter(
    "reco_requests_total",
    "Total recommendation requests"
)

LATENCY = Histogram(
    "reco_latency_seconds",
    "Recommendation latency"
)

ERRORS = Counter(
    "reco_errors_total",
    "Total recommendation errors"
)