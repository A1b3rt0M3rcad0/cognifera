from sqlalchemy import Engine
from abc import ABC, abstractmethod
from typing import Self

class IAsyncDBConnectionHandler(ABC):

    @abstractmethod
    def _create_database_engine(self) -> Engine:pass

    @abstractmethod
    def get_engine(self) -> Engine:pass

    @abstractmethod
    async def __aenter__(self) -> Self:pass

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:pass