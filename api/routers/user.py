from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..crud import user
from ..dependencies import get_db, oauth2_scheme
from ..schemas import user as user_schema

router = APIRouter(
    prefix="/user",
    tags=["user"],
    dependencies=[Depends(get_db), Depends(oauth2_scheme)],
    responses={404: {"description": "Not found"}},
)


# @router.get("/")
# async def read_users(
#     token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db)
# ):
#     return {"token": token}
#     users = user.get_users(db)
#     return users


# @router.get("/{user_id}")
# async def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = user.get_user(db, user_id)
#     if db_user:
#         return db_user
#     else:
#         raise HTTPException(status_code=404, detail="user not found")


# @router.post("/")
# async def create_user(user: user_schema.UserCreate, db: Session = Depends(get_db)):
#     db_user = user.get_user(db, user_id)
#     if db_user:
#         return db_user
#     else:
#         raise HTTPException(status_code=404, detail="user not found")
