from sqlalchemy import Column, DateTime, ForeignKey, Integer
from database import Base


class APIUsage(Base):
    __tablename__ = "api_usage"

    api_usage_id = Column(Integer, primary_key=True)
    api_id = Column(Integer, ForeignKey("api.api_id"))
    api_user_id = Column(Integer, ForeignKey("api_user.api_user_id"))
    timestamp = Column(DateTime)
    resonse_code = Column(Integer)
