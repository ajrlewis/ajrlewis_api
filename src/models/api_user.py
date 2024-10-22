from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class APIUser(Base):
    __tablename__ = "api_user"

    api_user_id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password_hash = Column(String)
    is_admin = Column(Boolean, default=False)
    api_key = Column(String)
    # api_credit_balance = Column(Integer, default=42069)
    # plan = Column(String, default="Free")
