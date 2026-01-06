import json
from datetime import datetime


def log_metrics(metrics: dict, path="metrics.json"):
    payload = {
        "timestamp": datetime.utcnow().isoformat(),
        "metrics": metrics
    }

    with open(path, "a") as f:
        f.write(json.dumps(payload) + "\n")