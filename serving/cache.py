import redis
import json

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

CACHE_TTL = 60  # seconds


def get_cached(key: str):
    data = redis_client.get(key)
    return json.loads(data) if data else None


def set_cached(key: str, value: dict):
    redis_client.setex(key, CACHE_TTL, json.dumps(value))