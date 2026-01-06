import joblib
from datetime import datetime
from pathlib import Path

MODEL_DIR = Path("models")


def register_model(model, metrics: dict, name="deepsequence"):
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M")
    model_path = MODEL_DIR / f"{name}_{timestamp}.pkl"

    MODEL_DIR.mkdir(exist_ok=True)
    joblib.dump(model, model_path)

    meta = {
        "model_path": str(model_path),
        "metrics": metrics,
        "registered_at": timestamp
    }

    return meta