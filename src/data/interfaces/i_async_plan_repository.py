from abc import ABC, abstractmethod
from src.domain.models.plan import Plan
from typing import Dict

class IAsyncPlanRepository(ABC):

    @abstractmethod
    async def insert(self, name:str, price:float, flash_card_limit_per_month:int, days:int) -> None:pass

    @abstractmethod
    async def select(self, name:str) -> Plan:pass

    @abstractmethod
    async def update(self, name:str, update_params:Dict) -> None:pass

    @abstractmethod
    async def delete(self, name:str) -> None:pass