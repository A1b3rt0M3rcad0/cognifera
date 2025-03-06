from src.infra.db.sql.config.connection.sqlite_connection_string import SQLiteConnectionString
from src.infra.db.sql.connection_handler.db_connection_handler import DBConnectionHandler
from sqlalchemy import text

def test_db_connection_handler() -> None:
    db_connection_handler = DBConnectionHandler(SQLiteConnectionString)
    engine = db_connection_handler.get_engine()
    
    assert engine
    assert hasattr(engine, "connect")

    with engine.connect() as cnx:
        result = cnx.execute(text("SELECT 1"))
        assert result.scalar() == 1