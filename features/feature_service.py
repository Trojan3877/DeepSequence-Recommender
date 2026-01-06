from online_store import read_features


def get_user_features(user_id: int):
    return read_features(f"user:{user_id}")


def get_item_features(item_id: int):
    return read_features(f"item:{item_id}")