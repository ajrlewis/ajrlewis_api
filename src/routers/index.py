from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# from ..dependencies import get_db
from dependencies import get_db


router = APIRouter(
    prefix="",
    tags=["index"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/ping")
async def status(db: Session = Depends(get_db)):
    try:
        _ = db.connection()
    except Exception as e:
        raise HTTPException(status_code=400, detail="Database unavailable")
    return {"data": "Pong"}
