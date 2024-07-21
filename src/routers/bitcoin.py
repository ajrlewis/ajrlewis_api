from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

# from ..dependencies import get_db
from dependencies import get_db


router = APIRouter(
    prefix="/bitcoin",
    tags=["Bitcoin"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/block-height")
async def block_height():
    """Reurns the block_height of the bitcoin block chain."""
    # bitcoinkit.get_block_heigh()
    return {"message": "Hello World"}


@router.get("/price/")
async def price():
    """Returns the current price in a supplied fiat currency."""
    # <ticker:str>
    # bitcoinkit.price("ticker")
    return {"message": "Hello World"}


@router.get("/quotes")
async def quotes():
    """Returns quotes from prominent figures throughout the history of Bitcoin."""
    return {"message": "Hello World"}


@router.get("/lightning")
async def lightning():
    return {"message": "Hello World"}


@router.get("/lightning/create")
async def lightning_create():
    return {"message": "Hello World"}


# @router.get("/cashu")
# async def cashu():
#     return {"message": "Hello World"}
