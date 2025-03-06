from abc import ABC, abstractmethod

class IDatabaseConnectionString(ABC):

    @classmethod
    @abstractmethod
    def get_sync_connection_string(cls) -> str:pass

    @classmethod
    @abstractmethod
    def get_async_connection_string(cls) -> str:pass