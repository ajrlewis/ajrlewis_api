import sys

# sys.path.append("../src")
sys.path.append("src")

from fastapi import FastAPI

# from .database import Base, engine
# from .routers import index, bitcoin, chat, data_analytics, forecast, image, web
from database import Base, engine
from routers import index, bitcoin, chat, data_analytics, forecast, image, web

Base.metadata.create_all(bind=engine)

app = FastAPI()

# from fastapi.responses import JSONResponse

# class UnicornException(Exception):
#     def __init__(self, name: str):
#         self.name = name

# @app.exception_handler(UnicornException)
# async def unicorn_exception_handler(request: Request, exc: UnicornException):
#     return JSONResponse(
#         status_code=418,
#         content={"error": {"message": f"Oops! Did something. There goes a rainbow..."}},
#     )


app.include_router(index.router)
app.include_router(bitcoin.router)
app.include_router(chat.router)
app.include_router(data_analytics.router)
app.include_router(forecast.router)
app.include_router(image.router)
app.include_router(web.router)
