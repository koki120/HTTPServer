from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1_STR: str = "api"
    # TODO:べた書きを直す。
    SECRET_KEY: str = "2e655e3f2e382d7978acf20bd90dbb911651c1c5d553a79101faa7c4c5dd5bf3"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7


settings = Settings()
