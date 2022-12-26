from pymongo import MongoClient
from pymongo.collection import Collection

from config.model import AppConfig


class Database:
    _instance: "Database" = None

    def __init__(self, config: AppConfig) -> None:
        self._client = MongoClient(config.db_connection_str)
        self.db = self._client[config.db_name]

    @staticmethod
    def initialize(config: AppConfig):
        if Database._instance is None:
            Database._instance = Database(config)
        else:
            raise SystemError(
                "Database is already initialized, use instance to get the database instance")

    @staticmethod
    def instance():
        if Database._instance is None:
            raise SystemError(
                "Database is not initialized use Database.initialize first")
        return Database._instance
