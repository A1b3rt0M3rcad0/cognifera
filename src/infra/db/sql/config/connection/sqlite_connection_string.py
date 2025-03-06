from src.infra.db.sql.config.interfaces.i_database_connection_string import IDatabaseConnectionString

class SQLiteConnectionString(IDatabaseConnectionString):

    connection_string = "sqlite:///src/infra/db/sql/test/database/database.db"

    @classmethod
    def get_connection_string(cls) -> str:
        if not cls.connection_string:
            raise ValueError("Connection String is NoneType")
        return cls.connection_string