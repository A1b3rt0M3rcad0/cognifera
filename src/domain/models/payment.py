#pylint:disable=R0902
from datetime import datetime
from dataclasses import dataclass
from enum import Enum

@dataclass
class Payment:

    id:str
    user_email: str
    plan_name: str
    amount: float
    payment_channel: str
    status: Enum
    transaction_id: str
    currency: str
    payment_method_details: str
    refund_status: Enum
    failure_reason: str
    payment_gateway: str
    payment_date: datetime
    created_at: datetime