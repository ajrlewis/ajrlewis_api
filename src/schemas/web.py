import datetime
from typing import Union

from pydantic import BaseModel, Field


class Web(BaseModel):
    website_id: int
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
