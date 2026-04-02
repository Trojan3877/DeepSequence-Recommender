"""Application settings loaded from environment variables."""

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    secret_key: str = Field(default="change-this-secret")
    redis_url: str = Field(default="redis://localhost:6379")
    mlflow_tracking_uri: str = Field(default="http://localhost:5000")
    environment: str = Field(default="development")
    log_level: str = Field(default="INFO")

    # Model hyper-parameters
    embedding_dim: int = 64
    hidden_dim: int = 128
    num_layers: int = 2
    max_sequence_length: int = 50
    top_k: int = 10

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
