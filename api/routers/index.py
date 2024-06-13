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


@router.get("/status")
async def status(db: Session = Depends(get_db)):
    try:
        _ = db.connection()
        return {"database": "Online", "server": "Online"}
    except Exception as e:
        return {"database": "Offline", "server": "Online"}


# def validate(session):
#     try:
#         # Try to get the underlying session connection, If you can get it, its up
#         connection = session.connection()
#         return True
#     except:
#         return False
