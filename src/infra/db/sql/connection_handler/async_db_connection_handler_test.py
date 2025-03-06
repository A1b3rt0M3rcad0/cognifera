from src.infra.db.sql.config.connection.sqlite_connection_string import SQLiteConnectionString
from src.infra.db.sql.connection_handler.async_db_connection_handler import AsyncDBConnectionHandler
from sqlalchemy import text
import pytest

@pytest.mark.asyncio
async def test_db_connection_handler() -> None:
    async_db_connection_handler = AsyncDBConnectionHandler(SQLiteConnectionString)
    engine = async_db_connection_handler.get_engine()
    
    assert engine
    assert hasattr(engine, "connect")

    async with engine.connect() as cnx:
        result = await cnx.execute(text("SELECT 1"))
        assert result.scalar() == 1