from src.infra.db.sql.config.interfaces.i_database_connection_string import IDatabaseConnectionString
import os

class MysqlConnectionString(IDatabaseConnectionString):

    connection_string = os.getenv("MYSQL_CONNECTION_STRING")

    @classmethod
    def get_connection_string(cls) -> str:
        if not cls.connection_string:
            raise ValueError("The environment variable 'MYSQL_CONNECTION_STRING' is not set.")
        return cls.connection_string