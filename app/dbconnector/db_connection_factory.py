from .db_connector_manager import DatabaseConnectionManager

class DatabaseConnectionManagerFactory:
    _manager_instances = {}

    @classmethod
    def get_instance(cls, db_url: str, pool_size=10, max_overflow=20):
        if db_url not in cls._manager_instances:
            cls._manager_instances[db_url] = DatabaseConnectionManager(db_url, pool_size, max_overflow)
        return cls._manager_instances[db_url]