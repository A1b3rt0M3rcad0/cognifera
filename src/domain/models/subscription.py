#pylint:disable=R0902
from datetime import datetime
from dataclasses import dataclass
from enum import Enum

@dataclass
class Subscription:

    id: int
    payment_id: int
    user_email: str
    plan_name: str
    start_date: datetime
    end_date: datetime
    usage_limite_date: datetime
    status: Enum
    created_at: datetime