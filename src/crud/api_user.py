import secrets
from typing import Optional

import bcrypt
from loguru import logger

from database import SessionLocal
from models import APIUser
from schemas.api_user import APIUserCreate


def get_api_user_by_api_key(db: SessionLocal, api_key: str) -> Optional[APIUser]:
    api_key = str(api_key)
    return db.query(APIUser).filter_by(api_key=api_key).first()


# def create_api_user(db: SessionLocal, user: user_schema.UserCreate) -> user_model.User:
#     # Check if the user already exists
#     db_user = get_user_by_username(db, user.username)
#     if db_user:
#         logger.debug(f"User exists: {db_user = }")
#         return db_user

#     # Hash the user password
#     password_hash = bcrypt.hashpw(user.password.encode("utf-8"), bcrypt.gensalt())

#     # Create new API key
#     api_key = f"sk-{secrets.token_urlsafe(32)}"

#     # Create the User
#     db_user = user_model.User(
#         username=user.username, password_hash=password_hash, api_key=api_key
#     )

#     # Add and commit the user to the database.
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)

#     return db_user
