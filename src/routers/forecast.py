from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field

# from ..dependencies import get_db
from dependencies import get_db


class Timeseries(BaseModel):
    x: list[int] = Field(None, description="The variable to forecast")
    y: list[float] = Field(None, description="The variable to forecast")


class HoltWintersParmeters(BaseModel):
    # fit
    alpha: float = 0.0
    beta: float = 0.0
    phi: float = 0.0
    gama: float = 0.0
    number_of_seasons: int = Field(
        None, description="The repetition frequeny of the underlying patter."
    )
    accuracy: float = 0.0


class HoltWinteForecastLatentVariables(BaseModel):
    level: float = 0.0
    trend: float = 0.0
    seasons: list[float] = [0, 0]


router = APIRouter(
    prefix="/forecast",
    tags=["Forecast"],
    dependencies=[Depends(get_db)],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def root():
    return {"message": "Hello World"}


@router.get("/naive")
async def naive(db: Session = Depends(get_db)):
    return {"result": []}


@router.get("/holt-winters")
async def holt_winters(db: Session = Depends(get_db)):
    return {"result": []}


@router.get("/holt-winters/fit")
async def holt_winters_fit(db: Session = Depends(get_db)):
    return {"result": []}


@router.get("/holt-winters/smooth")
async def holt_winters_smooth(db: Session = Depends(get_db)):
    return {"result": []}


@router.get("/seasonality")
async def seasonality(db: Session = Depends(get_db)):
    return {"result": []}
