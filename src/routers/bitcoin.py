import bitcoinkit
from fastapi import APIRouter, Depends, HTTPException
from loguru import logger
from sqlalchemy.orm import Session

from dependencies import get_db


router = APIRouter(prefix="/bitcoin", tags=["Bitcoin"])


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/block_height")
async def block_height():
    """Returns the Bitcoin block height"""
    timestamp = ""
    block_height = bitcoinkit.get_block_height(timestamp=timestamp)
    return {"timestamp": timestamp, "block_height": block_height}


@router.get("/price")
async def price():
    """Returns the price of 1 BTC in a given currency."""
    timestamp = ""
    currency = ""
    price = bitcoinkit.price(timestamp=timestamp, currency=currency)
    return {"timestamp": timestamp, "price": price, "currency": currency}


@router.get("/quotes")
async def quotes():
    """Returns quotes from prominent figures throughout the history of Bitcoin."""
    return {"message": "Hello World"}


# @router.get("/lightning")
# async def lightning():
#     return {"message": "Hello World"}

# @router.get("/cashu")
# async def cashu():
#     return {"message": "Hello World"}
