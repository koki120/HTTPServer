from pydantic import BaseSettings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DBSettings(BaseSettings):
    DB_USERNAME: str = "root"
    DB_PASSWORD: str = "test"
    DB_HOST: str = "mysql"
    DB_NAME: str = "dev"


settings = DBSettings()


DATABASE: str = "mysql://%s:%s@%s/%s?charset=utf8mb4" % (
    settings.DB_USERNAME,
    settings.DB_PASSWORD,
    settings.DB_HOST,
    settings.DB_NAME,
)

# DBとの接続
# TODO:開発終了時にFalseに戻す。
echo: bool = True  # 実行されたSQLを表示する
pool_recycle: int = 60 * 60 * 7  # 7時間でコネクションの貼り直し
ENGINE = create_engine(DATABASE, echo=echo, pool_recycle=pool_recycle)

# Sessionの作成
# ORM実行時の設定。自動コミットするか、自動反映するか
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)


SessionLocal()
