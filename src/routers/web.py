from typing import Union
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field

# from ..utils import web
from utils import web


class WebScraper(BaseModel):
    text: str = Field(None, description="The text content of the URL.")


router = APIRouter(
    prefix="/web",
    tags=["Web"],
)


@router.get("/scrape", response_model=WebScraper)
async def scrape(
    url: str = Query(
        None,
        description="The URL to web scrape.",
    ),
    max_words_in_text: int = Query(
        None,
        description="The maximum number of words in the text content to return. Leave empty to return all words.",
    ),
) -> WebScraper:
    """Scrapes the text content from a supplied website URL."""
    text, error = web.scrape_website_for_text(url)
    if error:
        raise HTTPException(status_code=400, detail=error)
    if max_words_in_text:
        words = text.split(" ")
        text = " ".join(words[:max_words_in_text])
    return {"text": text}


@router.get("/search")
async def search():
    return {"text": "Foo Bar"}
