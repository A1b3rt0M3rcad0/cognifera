from src.infra.db.sql.config.base_entity.base import Base
from src.infra.db.sql.entities.payment import Payment
from src.infra.db.sql.entities.plan import Plan
from src.infra.db.sql.entities.user import User
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Enum
from datetime import datetime, timezone
from sqlalchemy.orm import relationship
import enum

class Status(enum.Enum):

    ACTIVE = "active"
    CANCELED = "canceled"
    EXPIRED = "expired"
    DEACTIVE = "deactive"


class Subscription(Base):

    __tablename__ = 'subscription'

    id = Column(Integer, primary_key=True, autoincrement=True)
    payment_id = Column(Integer, ForeignKey("payment.id"), nullable=False)
    user_email = Column(String, ForeignKey("user.email"), nullable=False)
    plan_name = Column(String, ForeignKey("plan.name"), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    usage_limit_date = Column(DateTime, nullable=False)
    status = Column(Enum(Status), nullable=False, default=Status.DEACTIVE)
    created_at = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))

    user = relationship(User, backref=__tablename__)
    plan = relationship(Plan, backref=__tablename__)
    payment = relationship(Payment, backref=__tablename__)
