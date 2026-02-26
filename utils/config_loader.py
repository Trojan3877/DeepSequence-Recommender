import yaml
from pathlib import Path


class Config:
    def __init__(self, config_path: str = "config/settings.yaml"):
        self.config_path = Path(config_path)
        self._config = self._load_config()

    def _load_config(self):
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config file not found at {self.config_path}")
        with open(self.config_path, "r") as file:
            return yaml.safe_load(file)

    def get(self, key: str):
        return self._config.get(key)

    def __getitem__(self, key):
        return self._config[key]