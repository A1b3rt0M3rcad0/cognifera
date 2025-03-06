from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy import func
from src.infra.db.sql.config.base_entity.base import Base

class User(Base):

    __tablename__ = "user"

    email = Column(String, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    flash_card_generated_in_the_month = Column(Integer, nullable=False, default=0)
    created_at = Column(DateTime, default=func.now)
