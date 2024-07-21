from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    user_id: int
    password_hash: str
    api_key: str
    credits: int

    class Config:
        from_attributes = True
