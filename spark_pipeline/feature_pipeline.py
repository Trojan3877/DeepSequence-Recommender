from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lag
from pyspark.sql.window import Window


class FeaturePipeline:

    def __init__(self):
        self.spark = SparkSession.builder.appName(
            "DeepSequenceFeaturePipeline"
        ).getOrCreate()

    def load_from_snowflake(self, sf_options: dict, table_name: str):
        return (
            self.spark.read.format("snowflake")
            .options(**sf_options)
            .option("dbtable", table_name)
            .load()
        )

    def build_sequences(self, df):
        window = Window.partitionBy("user_id").orderBy("timestamp")
        df = df.withColumn("prev_item", lag("item_id").over(window))
        return df