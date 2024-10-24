from typing import Annotated, Union

from fastapi import APIRouter, HTTPException
from loguru import logger
from webkit import scrape as webkit_scrape, search as webkit_search

from dependencies import GetDBDep, GetCurrentUserDep
from schemas.web import Web, WebScrapeInput


router = APIRouter(prefix="/web", tags=["Web"])


@router.post("/scrape")
async def scrape(
    db: GetDBDep, user: GetCurrentUserDep, web_scrape_input: WebScrapeInput
) -> Web:
    """Scrapes the text content from a supplied website URL."""
    url = web_scrape_input.url
    logger.debug(f"{url = }")
    sanitized_url = webkit_scrape.sanitize_url(url)
    logger.debug(f"{sanitized_url = }")
    data = webkit_scrape.text_from_url(url)
    logger.debug(f"{data = }")
    return data


# @router.get("/search")
# async def search():
#     """Scrapes the internet for a given search query."""
#     data = search(text)
#     if data["error"]:
#         raise HTTPException(status_code=400, detail=data["error"])
#     return data
