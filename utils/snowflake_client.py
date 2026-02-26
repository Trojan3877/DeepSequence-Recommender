import snowflake.connector


class SnowflakeClient:

    def __init__(self, config):
        self.config = config
        self.conn = None

    def connect(self):
        self.conn = snowflake.connector.connect(
            account=self.config["account"],
            user=self.config["user"],
            warehouse=self.config["warehouse"],
            database=self.config["database"],
            schema=self.config["schema"]
        )

    def execute(self, query: str):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def close(self):
        if self.conn:
            self.conn.close()