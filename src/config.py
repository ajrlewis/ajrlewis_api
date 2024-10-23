import os

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = os.getenv("SQLALCHEMY_DATABASE_URL", "")
    PROJECT_NAME: str = os.getenv("PROJECT_NAME", "")
    PROJECT_DESCRIPTION: str = os.getenv("PROJECT_DESCRIPTION", "")
    PROJECT_SUMMARY: str = os.getenv("PROJECT_SUMMARY", "")
    PROJECT_VERSION: str = os.getenv("PROJECT_VERSION", "")
    PROJECT_LICENSE: str = os.getenv("PROJECT_LICENSE", "")
    PROJECT_LICENSE_URL: str = os.getenv("PROJECT_LICENSE_URL", "")


settings = Settings()
