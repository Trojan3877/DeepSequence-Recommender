import pandas as pd
import time


def build_user_features(events: pd.DataFrame) -> pd.DataFrame:
    now = time.time()

    features = events.groupby("user_id").agg(
        avg_watch_time=("watch_time", "mean"),
        clicks_7d=("clicked", "sum"),
        last_active_ts=("timestamp", "max")
    ).reset_index()

    features["recency_hours"] = (now - features["last_active_ts"]) / 3600
    return features


def build_item_features(events: pd.DataFrame) -> pd.DataFrame:
    now = time.time()

    features = events.groupby("item_id").agg(
        popularity_7d=("clicked", "sum"),
        ctr_30d=("clicked", "mean"),
        last_seen=("timestamp", "max")
    ).reset_index()

    features["freshness_hours"] = (now - features["last_seen"]) / 3600
    return features