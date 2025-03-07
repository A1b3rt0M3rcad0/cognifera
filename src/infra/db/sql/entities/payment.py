from src.infra.db.sql.config.base_entity.base import Base
from src.infra.db.sql.entities.user import User
from src.infra.db.sql.entities.plan import Plan
from sqlalchemy import Column, String, Integer, DateTime, Float, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from src.domain.status.payment_status import Status
from src.domain.status.payment_refund_status import RefundStatus

class Payment(Base):

    __tablename__ = "payment"

    id = Column(Integer, autoincrement=True, primary_key=True)
    user_email = Column(String, ForeignKey("user.email"))
    plan_name = Column(String, ForeignKey("plan.name"))
    amount = Column(Float, nullable=False)
    payment_channel = Column(String, nullable=False)
    status = Column(Enum(Status), nullable=False, default=Status.IN_PROGRESS)
    transaction_id = Column(String, nullable=False)
    currency = Column(String, nullable=False)
    payment_method_details = Column(String, nullable=True)
    refund_status = Column(Enum(RefundStatus), nullable=False, default=RefundStatus.NOT_REFUNDED)
    failure_reason = Column(String, nullable=False)
    payment_gateway = Column(String, nullable=False)
    payment_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now(timezone.utc))

    user = relationship(User, backref=__tablename__)
    plan = relationship(Plan, backref=__tablename__)