import secrets

import bcrypt
from loguru import logger

from database import SessionLocal
from models import user as user_model
from schemas import user as user_schema


def get_user_by_user_id(db: SessionLocal, user_id: int):
    logger.debug(f"{user_id = }")
    return db.query(user_model.User).get(user_id)


def get_user_by_username(db: SessionLocal, username: str):
    logger.debug(f"{username = }")
    return db.query(user_model.User).filter_by(username=username).first()


def get_user_by_api_key(db: SessionLocal, api_key: str):
    api_key = str(api_key)
    logger.debug(f"{api_key = } {type(api_key) = }")
    return db.query(user_model.User).filter_by(api_key=api_key).first()


def deduct_user_credits(db: SessionLocal, user: user_model.User, credits: int):
    logger.debug(f"{user = } {credits = }")
    user.credits -= credits
    logger.debug(f"{user.credits = }")
    db.commit()


def create_user(db: SessionLocal, user: user_schema.UserCreate) -> user_model.User:
    # Check if the user already exists
    db_user = get_user_by_username(db, user.username)
    if db_user:
        logger.debug(f"User exists: {db_user = }")
        return db_user

    # Hash the user password
    password_hash = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())

    # Create new API key
    api_key = f"sk-{secrets.token_urlsafe(32)}"

    # Create the User
    db_user = user_model.User(
        username=user.username, password_hash=password_hash, api_key=api_key
    )

    # Add and commit the user to the database.
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user
