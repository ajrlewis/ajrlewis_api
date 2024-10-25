from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class API(Base):
    __tablename__ = "api"

    api_id = Column(Integer, primary_key=True)
    endpoint = Column(String)
    method = Column(String, default="GET")
    credits = Column(Integer, default=420)
