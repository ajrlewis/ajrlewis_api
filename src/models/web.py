from sqlalchemy import Column
from sqlalchemy import Boolean, DateTime, Integer, String

from database import Base


class Web(Base):
    __tablename__ = "web"

    website_id = Column(Integer, primary_key=True)
    url = Column(String, unique=True)
    sanitized_url = Column(String)
    redirected_url = Column(String, nullable=True)
    text = Column(String, nullable=True)
    error = Column(String, nullable=True)
    is_reachable = Column(Boolean)
    scraped_on = Column(DateTime)
