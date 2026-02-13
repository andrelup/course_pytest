
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.settings.database import DatabaseSettings

engine = create_async_engine(DatabaseSettings.database_url)
async def get_session() -> AsyncSession:
    async_session_factory = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)
    async with async_session_factory() as session:
        yield session