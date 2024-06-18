from fastapi import FastAPI
from .database import Base, engine
from .routers import index, chat, web_scraper

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


# app.include_router(index.router)
app.include_router(chat.router)
app.include_router(web_scraper.router)
