from abc import ABC, abstractmethod
from src.domain.models.user import User
from typing import Dict

class IAsyncUserRepository(ABC):

    @abstractmethod
    async def insert(self, email:str, username:str, password:str, flash_card_generated_in_the_month:int) -> None:pass

    @abstractmethod
    async def select(self, email:str) -> User:pass

    @abstractmethod
    async def update(self, email:str, update_params:Dict) -> None:pass

    @abstractmethod
    async def delete(self, email:str) -> None:pass