from pydantic import BaseModel


class APIUserBase(BaseModel):
    username: str
    email: str


class APIUserCreate(APIUserBase):
    password: str


class APIUser(APIUserBase):
    api_user_id: int
    password_hash: str
    is_admin: bool
    api_key: str
    # credits: int
    # plan: str

    class Config:
        from_attributes = True
