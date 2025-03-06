from datetime import datetime
from dataclasses import dataclass

@dataclass
class User:

    email:str
    username:str
    password:str
    flash_card_generated_in_the_month:int
    created_at:datetime