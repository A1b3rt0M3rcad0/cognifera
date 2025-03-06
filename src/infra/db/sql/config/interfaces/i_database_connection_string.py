from abc import ABC, abstractmethod

class IDatabaseConnectionString(ABC):

    @classmethod
    @abstractmethod
    def get_connection_string(cls) -> str:pass