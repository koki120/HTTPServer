from pydantic import BaseSettings
import secrets


class Settings(BaseSettings):
    #  環境変数は常にenvファイルからロードされた値よりも優先される。
    API_V1_STR: str = "api"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7


settings = Settings()
