from typing import Union
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from ..utils import web_scraper


class WebScraper(BaseModel):
    text: str = Field(None, description="The text content of the URL.")


router = APIRouter(
    prefix="/web-scraper",
    tags=["Web Scraper"],
)


@router.get("/", response_model=WebScraper)
async def root(
    url: str = Query(
        None,
        description="The URL to web scrape.",
    ),
    max_words_in_text: int = Query(
        None,
        description="The maximum number of words in the text content to return. Leave empty to return all words.",
    ),
) -> WebScraper:
    """Retrieves the text content from a website URL using a web scraper."""
    text, error = web_scraper.scrape_website_for_text(url)
    if error:
        raise HTTPException(status_code=400, detail=error)
    if max_words_in_text:
        words = text.split(" ")
        text = " ".join(words[:max_words_in_text])
    return {"text": text}
