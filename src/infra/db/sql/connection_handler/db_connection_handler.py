from src.infra.db.sql.interfaces.i_db_connection_handler import IDBConnectionHandler
from src.infra.db.sql.config.interfaces.i_database_connection_string import IDatabaseConnectionString
from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from typing import Self


class DBConnectionHandler(IDBConnectionHandler):

    def __init__(self, string_connection:IDatabaseConnectionString) -> None:
        self.__connection_string = string_connection.get_connection_string()
        self.__engine = self._create_database_engine()
        self.session = None
    
    def _create_database_engine(self) -> Engine:
        return create_engine(self.__connection_string)
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self) -> Self:
        session_make = sessionmaker(self.__engine)
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.session.close()