from dotenv import find_dotenv
from pydantic import BaseSettings

from pathlib import Path
import sqlite3

# Ruta al archivo pytest.db en la raiz del proyecto
# db_path = Path(__file__).resolve().parents[1] / "pytest.db"

# Conectar (crea el archivo si no existe)
conn = sqlite3.connect("pytest.db")
cursor = conn.cursor()

class BaseProjectSettings(BaseSettings):

    class Config:
        env_file = find_dotenv(filename=".env.local")