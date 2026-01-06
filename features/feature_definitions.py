from dataclasses import dataclass


@dataclass
class UserFeatures:
    user_id: int
    avg_watch_time: float
    clicks_7d: int
    last_active_ts: float


@dataclass
class ItemFeatures:
    item_id: int
    popularity_7d: int
    ctr_30d: float
    freshness_hours: float