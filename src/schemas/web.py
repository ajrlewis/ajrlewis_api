import datetime
from typing import Union

from pydantic import BaseModel, Field


class Web(BaseModel):
    # website_id: int
    url: str
    sanitized_url: str
    redirected_url: Union[str, None] = None
    text: Union[str, None] = None
    error: Union[str, None] = None
    is_reachable: bool
    scraped_on: datetime.datetime

    class Config:
        from_attributes = True


class WebScrapeInput(BaseModel):
    url: str = Field("ajrlewis.com", description="The URL to web scrape.")


class WebSearchInput(BaseModel):
    keywords: str = Field(
        "Satoshi Nakamoto", description="The keywords to search, i.e. the search query."
    )
    max_results: int = Field(5, description="The number of search results to return.")


class WebSearchResult(BaseModel):
    title: str
    href: str
    body: str


WebSearchResults = list[WebSearchResult]

WebSearchOutput = WebSearchResults
