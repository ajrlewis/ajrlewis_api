from fastapi import FastAPI
from .database import Base, engine
from .routers import index, user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(index.router)
app.include_router(user.router)
