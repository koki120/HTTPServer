from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.config.config import settings
from jose import JWTError, jwt
from app.usecases.user import UserUsecase
from app.domain.entities.user import User

from app.drivers.rdb.base import SessionLocal
from sqlalchemy import text

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/auth/access-token/"
)

uu = UserUsecase()



session = SessionLocal()

# # # 接続を確認するために、データベースのバージョン情報を取得します
query = text("SELECT VERSION()")
result = session.execute(query)
# print("データベースのバージョン:", result[0])
# # # セッションをクローズします
# session.close()
# print("接続確認が成功しました")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms="HS256")
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
        token_data_user_id = user_id
    except JWTError:
        raise credentials_exception
    user = uu.get_user(user_id=token_data_user_id)
    if user is None:
        raise credentials_exception
    return User(
        user_id=user.user_id,
        last_name=user.last_name,
        email=user.email,
        first_name=user.first_name,
        is_active=user.is_active,
        password="",
    )
