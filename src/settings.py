import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = os.getenv("SQLALCHEMY_DATABASE_URL")
