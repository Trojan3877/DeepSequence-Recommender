import redis

cache = redis.Redis(host="localhost", port=6379)

def get_cached(user_id):
    return cache.get(user_id)

def set_cached(user_id, preds):
    cache.set(user_id, str(preds))
