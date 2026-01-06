import redis
import json

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)


def write_features(key: str, features: dict):
    redis_client.set(key, json.dumps(features))


def read_features(key: str):
    data = redis_client.get(key)
    return json.loads(data) if data else None