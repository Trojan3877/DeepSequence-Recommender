from drift_detection import detect_drift


def should_retrain(reference_metrics, current_metrics):
    return detect_drift(
        reference_metrics["ctr"],
        current_metrics["ctr"]
    )