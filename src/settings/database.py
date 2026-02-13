from typing import Optional
from pydantic import SecretStr
from src.settings.base_settings import BaseProjectSettings


class _DatabaseSettings(BaseProjectSettings):
    """Configuración de la base de datos."""
    # database_url: str = "postgresql://postgres:pytest1234@localhost:5432/postgres"
    DB_DIALECT: str = "postgresql"
    DB_DRIVER: Optional[str]
    DB_USER: str
    DB_PASSWORD: SecretStr
    DB_HOST: str 
    DB_PORT: Optional[int]
    DB_NAME: str

    def build_url(self) -> str:
        return (
            "{dialect}{driver}://{username}:{password}@{host}:{port}/{name}".format(
                dialect=self.DB_DIALECT,
                driver="+" + self.DB_DRIVER if self.DB_DRIVER else "",
                username=self.DB_USER,
                password=self.DB_PASSWORD.get_secret_value(),
                host=self.DB_HOST,
                port=f"{self.DB_PORT}" if self.DB_PORT else "",
                name=self.DB_NAME
            )
        )
    
DatabaseSettings = _DatabaseSettings()