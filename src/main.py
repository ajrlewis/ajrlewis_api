logger.debug("Start of main.py")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from routers import index

# from routers import index, user, web

# from database import Base, engine
# from models.user import User
# Base.metadata.create_all(bind=engine)
logger.debug("Creating application ...")

app = FastAPI()
# app = FastAPI(title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json")

logger.debug("Assigning CORS middleware..")
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


logger.debug("Assigning routes ...")
app.include_router(index.router)
# app.include_router(user.router)
# app.include_router(bitcoin.router)
# app.include_router(chat.router)
# app.include_router(data_analytics.router)
# app.include_router(forecast.router)
# app.include_router(image.router)
# app.include_router(nostr.router)
# app.include_router(pdf.router)
# app.include_router(web.router)

logger.debug("Finished and ready!")
