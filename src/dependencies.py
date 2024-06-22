from typing import Annotated
from fastapi import Header, HTTPException
from fastapi.security import OAuth2PasswordBearer

# from .database import SessionLocal
from database import SessionLocal

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# SessionDependency = Annotated[Session, Depends(get_db)]
# TokenDep = Annotated[str, Depends(reusable_oauth2)]
