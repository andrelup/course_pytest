from dotenv import find_dotenv
from pydantic import BaseSettings

from pathlib import Path
import sqlite3

#  Conectar (crea el archivo si no existe)
# conn = sqlite3.connect("pytest.db")
# cursor = conn.cursor()

class BaseProjectSettings(BaseSettings):

    class Config:
        # Busca .env.local desde el directorio actual hacia arriba
        env_file = find_dotenv(".env.local", raise_error_if_not_found=True, usecwd=False)
        env_file_encoding = 'utf-8'