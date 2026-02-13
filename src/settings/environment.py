
from typing import Optional
import asyncpg
from pydantic import SecretStr
from src.settings.base_settings import BaseProjectSettings


class _EnvironmentSettings(BaseProjectSettings): 
    ENVIRONMENT: str
    DB_DIALECT: str 
    DB_DRIVER: Optional[str]
    DB_USER: str
    DB_PASSWORD: SecretStr
    DB_HOST: str 
    DB_PORT: Optional[int]
    DB_NAME: str


EnvironmentSettings = _EnvironmentSettings()    