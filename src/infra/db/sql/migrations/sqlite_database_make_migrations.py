from src.infra.db.sql.config.connection.sqlite_connection_string import SQLiteConnectionString
from src.infra.db.sql.migrations.make_migrations import Migrations

def make_migrations() -> None:
    Migrations.make_migrations(SQLiteConnectionString)

if __name__ == '__main__':
    make_migrations()