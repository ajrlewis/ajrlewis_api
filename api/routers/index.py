from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..crud import user
from ..dependencies import get_db


router = APIRouter(
    prefix="",
    tags=["index"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def root():
    return {"message": "Hello World"}
