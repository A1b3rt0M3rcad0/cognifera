from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from src.infra.db.sql.config.interfaces.i_database_connection_string import IDatabaseConnectionString
from src.infra.db.sql.interfaces.i_async_db_connection_handler import IAsyncDBConnectionHandler
from typing import Self


class AsyncDBConnectionHandler(IAsyncDBConnectionHandler):

    def __init__(self, string_connection:IDatabaseConnectionString) -> None:
        self.__connection_string = string_connection.get_async_connection_string()
        self.__engine = self._create_database_engine()
        self.session = None
    
    def _create_database_engine(self) -> Engine:
        return create_async_engine(self.__connection_string)
    
    def get_engine(self):
        return self.__engine
    
    async def __aenter__(self) -> Self:
        session_make = sessionmaker(self.__engine, class_= AsyncSession, expire_on_commit=False)
        self.session = session_make()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self.session.close()