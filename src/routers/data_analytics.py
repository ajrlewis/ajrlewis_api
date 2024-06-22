from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# from ..dependencies import get_db
from dependencies import get_db


# expects model of x, dx, yx, dy, t

# depends on get_seed a random value based on a lot of things, ;pcl joejbt o[ to,e etc/]
router = APIRouter(
    prefix="/data-analytics",
    tags=["Data Analytics"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.get("/mean/")
async def mean():
    return {"message": "Hello World"}


@router.get("/median")
async def median():
    return {"message": "Hello World"}


@router.get("/std-dev")
async def std_dev():
    return {"message": "Hello World"}
