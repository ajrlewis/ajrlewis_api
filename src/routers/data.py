import datakit
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db
from schemas.data import DataForecastInput, DataForecastOutput

router = APIRouter(prefix="/data", tags=["Data"])


@router.get("/stats")
async def stats(data_stats_input: dataStatsInput) -> DatatStatsOutput:
    y = data_stats_input.y
    mean = datakit.stats.mean(y)
    std_dev = datakit.stats.std_dev(y)
    median = datakit.stats.median(y)
    median_abs_dev = datakit.stats.median_abs_dev(y)
    data = datakit.stats.compute(y)
    return data


@router.get("/forecast")
async def forecast(data_forecast_input: DataForecastInput) -> DataForecastOutput:
    x_train = data_forecast_input.x_train
    y_train = data_forecast_input.y_train
    x_test = data_forecast_input.x_test
    y_test = data_forecast_input.y_test
    y_test, y_forecast = datakit.forecast.profet(
        x_train, y_train, x_test, y_test, x_forecast
    )
    return {"x_forecast": x_forecast, "y_forecast": y_forecast}
