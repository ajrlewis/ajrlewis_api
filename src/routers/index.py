from typing import Annotated

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from loguru import logger

from dependencies import GetDBDep, GetCurrentUserDep


router = APIRouter(
    prefix="",
    tags=["Index"],
    responses={403: {"description": "Not found"}, 404: {"description": "Not found"}},
)


@router.get("/")
async def root() -> str:
    """Returns 'Hello World'."""
    return "Hello World"
    # return {"message": "Hello World"}


# @router.get("/ping")
# async def ping(db: GetDBDep, user: GetCurrentUserDep):
#     logger.debug(f"{user = }")
#     try:
#         _ = db.connection()
#     except Exception as e:
#         raise HTTPException(status_code=400, detail="Database unavailable")
#     return {"message": "Pong"}
