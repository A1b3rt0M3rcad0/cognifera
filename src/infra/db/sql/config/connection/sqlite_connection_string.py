from src.infra.db.sql.config.interfaces.i_database_connection_string import IDatabaseConnectionString

class SQLiteConnectionString(IDatabaseConnectionString):

    async_connection_string = "sqlite+aiosqlite:///src/infra/db/sql/test/database/database.db"

    sync_connection_string = "sqlite:///src/infra/db/sql/test/database/database.db"

    @classmethod
    def get_async_connection_string(cls) -> str:
        if not cls.async_connection_string:
            raise ValueError("Connection String is NoneType")
        return cls.async_connection_string
    
    @classmethod
    def get_sync_connection_string(cls) -> str:
        if not cls.sync_connection_string:
            raise ValueError("Connection String is NoneType")
        return cls.sync_connection_string