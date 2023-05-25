from typing import Union
import app.drivers.security as security
from app.domain.entities.user import UserInDB


class UserUsecase:
    def __init__(self) -> None:
        self.db = {
            "nakatu": {
                "user_id": "nakatu",
                "first_name": "nakatsu",
                "email": "nakatu@example.com",
                "last_name": "fakehashedsecret",
                "is_active": True,
                "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
            },
            "alice": {
                "user_id": "alice",
                "first_name": "Alice",
                "email": "nakatu@example.com",
                "last_name": "Wonderson",
                "is_active": False,
                "hashed_password": "fakehashedsecret2",
            },
        }

    def get_user(self, user_id: str) -> UserInDB:
        if user_id in self.db:
            user_dict = self.db[user_id]
        return UserInDB(**user_dict)

    def authenticate(self, user_id: str, password: str) -> Union[UserInDB, None]:
        user = self.get_user(user_id)
        if user is None:
            return user
        if (
            security.verify_password(
                password=password, hashed_password=user.hashed_password
            )
            is False
        ):
            return None
        return user
