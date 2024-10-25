from typing import Annotated

from fastapi import Depends, Header, HTTPException, UploadFile, File
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
import imagekit
from loguru import logger

import crud.api_user as api_user_crud
from database import SessionLocal
from models.api_user import APIUser

GetCredentialsDep = Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())]


async def load_image(file: UploadFile = File(...)) -> imagekit.Image:
    logger.debug(f"{file = } {file.content_type = }")
    allowed_content_types = ("image/png", "image/jpeg", "image/jpg")
    if file.content_type not in allowed_content_types:
        detail = f"Only {allowed_content_types} allowed"
        logger.error(f"{detail = }")
        raise HTTPException(status_code=400, detail=detail)
    img = imagekit.load(await file.read())
    logger.debug(f"{img = }")
    return img


LoadImageDep = Annotated[imagekit.Image, Depends(load_image)]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


GetDBDep = Annotated[SessionLocal, Depends(get_db)]


async def current_user(db: GetDBDep, credentials: GetCredentialsDep):
    api_key = credentials.credentials
    api_user = api_user_crud.get_api_user_by_api_key(db, api_key)
    logger.debug(f"{api_user = }")
    if api_user:
        return api_user
    else:
        raise HTTPException(status_code=400, detail="Unauthorized")


GetCurrentUserDep = Annotated[APIUser, Depends(current_user)]
