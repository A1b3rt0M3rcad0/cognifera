from src.infra.db.sql.config.interfaces.i_database_connection_string import IDatabaseConnectionString
import os

class MysqlConnectionString(IDatabaseConnectionString):

    async_connection_string = os.getenv("ASYNC_MYSQL_CONNECTION_STRING")

    sync_connection_string = os.getenv("SYNC_MYSQL_CONNECTION_STRING")

    @classmethod
    def get_async_connection_string(cls) -> str:
        if not cls.async_connection_string:
            raise ValueError("The environment variable 'ASYNC_MYSQL_CONNECTION_STRING' is not set.")
        return cls.async_connection_string
    
    @classmethod
    def get_sync_connection_string(cls) -> str:
        if not cls.async_connection_string:
            raise ValueError("The environment variable 'SYNC_MYSQL_CONNECTION_STRING' is not set.")
        return cls.async_connection_string