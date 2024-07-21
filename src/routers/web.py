from typing import Annotated, Union

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field
from webkit import webkit

from schemas.website import Website


router = APIRouter(prefix="/web", tags=["Web"])


@router.get("/scrape", response_model=Website)
async def scrape(
    url: Annotated[str, Query(description="The URL to web scrape.")],
    max_words_in_text: Annotated[
        Union[int, None],
        Query(
            title="test",
            description="The maximum number of words in the text content to return. Leave empty to return all words.",
        ),
    ] = None,
):
    """Scrapes the text content from a supplied website URL."""
    data = webkit.scrape_website_for_text(url)
    if data["error"]:
        raise HTTPException(status_code=400, detail=data["error"])
    if max_words_in_text:
        words = data["text"].split(" ")
        data["text"] = " ".join(words[:max_words_in_text])
    return data
