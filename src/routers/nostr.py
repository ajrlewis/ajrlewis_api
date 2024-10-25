from fastapi import APIRouter, Depends, HTTPException
from loguru import logger
import nostrkit
from sqlalchemy.orm import Session

router = APIRouter(prefix="/nostr", tags=["Nostr"])


@router.get("/")
async def root():
    return {"message": "Hello World"}
