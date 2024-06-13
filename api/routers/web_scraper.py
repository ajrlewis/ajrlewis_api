from fastapi import APIRouter, HTTPException
from ..utils import web_scraper

router = APIRouter(
    prefix="/web-scraper",
    tags=["web-scraper"],
)


@router.get("/")
async def get(url: str) -> dict[str, str]:
    """Retrieve text content from a website URL using a web scraper."""
    text, error = web_scraper.scrape_website_for_text(url)
    if error:
        raise HTTPException(status_code=400, detail=error)
    return {"text": text}
