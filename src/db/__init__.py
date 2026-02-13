
from sqlalchemy.ext.asyncio import create_async_engine
from src.settings.database import Database_settings, DatabaseSettings

engine= create_async_engine(Database_settings.database_url, echo=True)