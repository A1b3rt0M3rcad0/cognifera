from datetime import datetime
from dataclasses import dataclass

@dataclass
class Plan:

    name: str
    price: float
    flash_card_limit_per_month: int
    days: int
    created_at: datetime