from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.domain.entities import auth
from app.config.config import settings
import app.drivers.security as security
from app.usecases.user import UserUsecase
from app.api.deps import get_current_user
from app.domain.entities.user import User

router = APIRouter()

uu = UserUsecase()


@router.post("/access-token")
async def login_access_token(
    credential: OAuth2PasswordRequestForm = Depends(),
) -> auth.Token:
    # usecaseに切り出し、errを返させる。
    user = uu.authenticate(user_id=credential.username, password=credential.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires: timedelta = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    access_token = security.create_access_token(
        subject=user.user_id, expires_delta=access_token_expires
    )
    return auth.Token(access_token=access_token, token_type="bearer")


# /users/me
@router.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)) -> User:
    return current_user
