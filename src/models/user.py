from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password_hash = Column(String)
    api_key = Column(String)
    credits = Column(Integer, default=5000)
    plan = Column(String, default="Free")

    def __repr__(self):
        return f"<User {self.user_id}>"
