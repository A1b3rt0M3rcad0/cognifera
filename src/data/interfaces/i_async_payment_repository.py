from abc import ABC, abstractmethod
from src.domain.models.payment import Payment
from typing import Dict
from typing import List
from datetime import datetime


class IAsyncPaymentRepository(ABC):

    @abstractmethod
    async def insert(self, 
    user_email: str,
    plan_name: str,
    amount: float,
    payment_channel: str,
    transaction_id: str,
    currency: str,
    payment_method_details: str,
    failure_reason: str,
    payment_gateway: str,
    payment_date: datetime,
    ) -> None: pass

    @abstractmethod
    async def select(self, select_params: Dict) -> List[Payment]: pass

    @abstractmethod
    async def update(self, select_params: Dict, update_params: Dict) -> None: pass

    @abstractmethod
    async def delete(self, payment_params: Dict) -> None: pass