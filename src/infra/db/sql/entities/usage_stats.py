from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import relationship
from src.infra.db.sql.entities.user import User
from src.infra.db.sql.config.base_entity.base import Base

class UsageStats(Base):

    __tablename__ = "usage_stats"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_email = Column(String, ForeignKey("user.email"))
    total_fashcards_generated = Column(Integer, nullable=False, default=0)
    total_videos_uploaded = Column(Integer, nullable=False, default=0)
    total_documents_uploaded = Column(Integer, nullable=False, default=0)
    last_active_at = Column(DateTime, default=func.now, onupdate=func.now)

    user = relationship(User, backref=__tablename__)