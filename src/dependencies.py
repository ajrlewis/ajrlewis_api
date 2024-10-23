from typing import Annotated

from fastapi import Depends, Header, HTTPException, UploadFile, File
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

# from imagekit import imagekit
from loguru import logger

import crud.api_user as api_user_crud
from database import SessionLocal
from models.api_user import APIUser

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
    api_key = credentials.credentials
    api_user = api_user_crud.get_api_user_by_api_key(db, api_key)
    logger.debug(f"{api_user = }")
    if api_user:
        return api_user
    else:
        raise HTTPException(status_code=400, detail="Unauthorized")


GetCurrentUserDep = Annotated[APIUser, Depends(current_user)]
