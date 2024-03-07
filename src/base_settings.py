import os
from typing import Optional

from dotenv import load_dotenv
from pydantic import (
    BaseModel,
)
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

load_dotenv('../ops/environment/.postgres.env')
load_dotenv('../ops/environment/.default.env')


class PostgresSettings(BaseModel):
    user: str = os.environ.get('POSTGRES_USER')
    password: str = os.environ.get('POSTGRES_PASSWORD')
    db: str = os.environ.get('POSTGRES_DB')
    host: str = 'localhost'
    port: str = 5432
    url: str = os.environ.get('POSTGRES__URL')


class ProjectSettings(BaseSettings):
    api_key: str
    debug: Optional[bool] = True

    postgres: PostgresSettings = PostgresSettings()

    date_time_format: str = '%Y-%m-%d %H:%M:%S'

    model_config = SettingsConfigDict(
        env_nested_delimiter='__',
        frozen=True,
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )


base_settings = PostgresSettings()
