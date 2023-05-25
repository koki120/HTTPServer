from pydantic import BaseModel
from typing import Union


class UserBase(BaseModel):
    user_id: str
    email: str
    first_name: Union[str, None] = None
    last_name: Union[str, None] = None
    is_active: bool


class User(UserBase):
    password: str


class UserInDB(UserBase):
    hashed_password: str
