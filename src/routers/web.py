from typing import Annotated, Union

from fastapi import APIRouter, HTTPException
from loguru import logger
import webkit

from dependencies import GetDBDep, GetCurrentUserDep
from schemas.web import Web, WebScrapeInput, WebSearchInput


router = APIRouter(prefix="/web", tags=["Web"])


@router.post("/scrape")
async def scrape(
    db: GetDBDep, user: GetCurrentUserDep, web_scrape_input: WebScrapeInput
) -> Web:
    """Scrapes the text content from a supplied website URL."""
    url = web_scrape_input.url
    logger.debug(f"{url = }")
    data = webkit.scrape.text_from_url(url)
    logger.debug(f"{data = }")
    return data


@router.post("/search")
async def search(
    db: GetDBDep, user: GetCurrentUserDep, web_search_input: WebSearchInput
) -> dict:
    """Searches the internet for a given"""
    keywords = web_search_input.keywords
    max_results = web_search_input.max_results
    logger.debug(f"{keywords = } {max_results = }")
    results = webkit.search.duckduckgo_search(
        keywords=keywords, max_results=max_results
    )
    logger.debug(f"{results = }")
    return {"foo": "bar"}
