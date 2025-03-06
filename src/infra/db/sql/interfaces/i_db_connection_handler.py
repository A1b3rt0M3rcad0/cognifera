from sqlalchemy import Engine
from abc import ABC, abstractmethod
from typing import Self

class IDBConnectionHandler(ABC):

    @abstractmethod
    def _create_database_engine(self) -> Engine:pass

    @abstractmethod
    def get_engine(self) -> Engine:pass

    @abstractmethod
    def __enter__(self) -> Self:pass

    @abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:pass