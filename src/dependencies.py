from typing import Annotated

from fastapi import Depends, Header, HTTPException, UploadFile, File
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from loguru import logger

# from imagekit import imagekit

import crud.user as user_crud
from database import SessionLocal
import models.user as user_model

GetCredentialsDep = Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())]


# async def load_image(file: UploadFile = File(...)):
#     logger.debug(f"{file.content_type = }")
#     if file.content_type != "image/png":
#         raise HTTPException(status_code=400, detail="Only PNG images are allowed")
#     logger.debug(f"{file = }")
#     img = imagekit.load(await file.read())
#     return img


# LoadImageDep = Annotated[imagekit.Img, Depends(load_image)]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


GetDBDep = Annotated[SessionLocal, Depends(get_db)]


async def current_user(db: GetDBDep, credentials: GetCredentialsDep):
    logger.debug(f"{credentials = }")
    api_key = credentials.credentials
    logger.debug(f"{api_key = }")
    db_user = user_crud.get_user_by_api_key(db, api_key)
    logger.debug(f"{db_user = }")
    if db_user:
        return db_user
    else:
        raise HTTPException(status_code=400, detail="Unauthorized")


GetCurrentUserDep = Annotated[user_model.User, Depends(current_user)]
