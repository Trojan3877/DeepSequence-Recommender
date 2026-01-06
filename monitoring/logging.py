import logging
import json

logging.basicConfig(level=logging.INFO)

def log_event(event_type: str, payload: dict):
    logging.info(json.dumps({
        "event": event_type,
        "payload": payload
    }))