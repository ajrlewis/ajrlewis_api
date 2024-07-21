from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field


class Timeseries(BaseModel):
    x: list[int] = Field(None, description="The variable to forecast")
    y: list[float] = Field(None, description="The variable to forecast")


router = APIRouter(
    prefix="/forecast",
    tags=["Forecast"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def root():
    """Trains and forecasts"""
    return {"message": "Hello World"}


@router.get("/train")
async def train():
    """Trains and returns a model for forecasting."""
    return {"model": []}
