from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger

# from routers import index, user, web
# from routers import index, user, web
from routers import chat, index, web

# from database import Base, engine
# from models.user import User
# Base.metadata.create_all(bind=engine)
from config import settings

logger.debug("Creating application ...")
app = FastAPI(
    docs_url="/docs",
    redoc_url=None,
    # docs_url=None,
    # redoc_url="/docs",
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESCRIPTION,
    summary=settings.PROJECT_SUMMARY,
    version=settings.PROJECT_VERSION,
    # terms_of_service="http://example.com/terms/",
    contact={
        # "name": "Deadpoolio the Amazing",
        # "url": "http://x-force.example.com/contact/",
        # "email": "dp@x-force.example.com",
    },
    license_info={
        "name": settings.PROJECT_LICENSE,
        "url": settings.PROJECT_LICENSE_URL,
    },
)


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
app.include_router(chat.router)
# app.include_router(bitcoin.router)
# app.include_router(chat.router)
# app.include_router(data_analytics.router)
# app.include_router(forecast.router)
# app.include_router(image.router)
# app.include_router(nostr.router)
# app.include_router(pdf.router)
app.include_router(web.router)
