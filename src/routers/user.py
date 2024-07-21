from typing import Annotated, Union
from fastapi import APIRouter, Depends, HTTPException, Query
from loguru import logger

from crud import user as user_crud
from dependencies import GetDBDep, GetCurrentUserDep
from schemas import user as user_schema


router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}},
)


# response_model=user_schema.User
@router.post("/")
async def create_user(db: GetDBDep, user: user_schema.UserCreate):
    logger.debug(f"{user = }")
    db_user = user_crud.create_user(db, user)
    logger.debug(f"{db_user = }")
    if db_user:
        return db_user
    else:
        raise HTTPException(status_code=404, detail="user not added")


# response_model=user_schema.User
@router.get("/")
async def get_users(
    db: GetDBDep,
    user_id: Annotated[Union[int, None], Query(description="The user ID to fetch..")],
):
    db_user = user_crud.get_user_by_user_id(db, user_id)
    logger.debug(f"{db_user = }")
    if db_user:
        return db_user
    else:
        raise HTTPException(status_code=404, detail="user not added")


@router.get("/credits")
async def get_user_credits(db: GetDBDep, user: GetCurrentUserDep):
    logger.debug(f"{db = }")
    logger.debug(f"{user = }")
    logger.debug(f"{user.credits = }")
    if user:
        # return {"username": user.username, "credits": user.credits}
        return user.credits
    else:
        raise HTTPException(status_code=404, detail="User not found!")


@router.post("/deduct")
async def deduct_user_credits(db: GetDBDep, user: GetCurrentUserDep, credits: int):
    user_crud.deduct_user_credits(db, user, credits)
    return user.credits
