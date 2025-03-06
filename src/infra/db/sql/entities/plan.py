from src.infra.db.sql.config.base_entity.base import Base
from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy import func

class Plan(Base):

    __tablename__ = "plan"

    name = Column(String, primary_key=True)
    price = Column(Float, nullable=False)
    flash_card_limit_per_month = Column(Integer, nullable=False)
    days = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now)