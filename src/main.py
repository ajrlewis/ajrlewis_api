from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

from config import settings
from routers import index
from routers import chat
from routers import web
from routers import image

# from routers import data
# from routers import bitcoin
# from routers import nostr

logger.debug("Creating application ...")
app = FastAPI(
    docs_url="/docs",
    redoc_url=None,
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    summary=settings.PROJECT_SUMMARY,
    version=settings.PROJECT_VERSION,
    # terms_of_service=settings.PROJECT_TERMS_OF_SERVICE,
    # contact={
    #     "name": settings.PROJECT_CONTACT_NAME
    #     "url": settings.PROJECT_CONTACT_URL,
    #     "email": settings.PROJECT_CONTACT_EMAIL,
    # },
    license_info={
        "name": settings.PROJECT_LICENSE,
        "url": settings.PROJECT_LICENSE_URL,
    },
)

logger.debug("Adding CORS middleware ...")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

logger.debug("Including routes ...")
app.include_router(index.router)
app.include_router(chat.router)
app.include_router(web.router)
app.include_router(image.router)
# app.include_router(data.router)
# app.include_router(bitcoin.router)
# app.include_router(nostr.router)
