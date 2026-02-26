import datetime
from utils.snowflake_client import SnowflakeClient


class EvaluationLogger:

    def __init__(self, sf_config):
        self.client = SnowflakeClient(sf_config)
        self.client.connect()

    def log_metrics(self, metrics: dict, model_version: str):
        timestamp = datetime.datetime.utcnow()

        insert_query = f"""
        INSERT INTO MODEL_EVALUATION_LOGS
        (timestamp, model_version, recall_at_10, precision_at_10, ndcg_at_10, hitrate_at_10)
        VALUES (
            '{timestamp}',
            '{model_version}',
            {metrics['Recall@10']},
            {metrics['Precision@10']},
            {metrics['NDCG@10']},
            {metrics['HitRate@10']}
        )
        """

        self.client.execute(insert_query)

CREATE TABLE MODEL_EVALUATION_LOGS (
    timestamp TIMESTAMP,
    model_version STRING,
    recall_at_10 FLOAT,
    precision_at_10 FLOAT,
    ndcg_at_10 FLOAT,
    hitrate_at_10 FLOAT
);