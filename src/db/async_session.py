
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from src.settings.database import DatabaseSettings

engine = create_async_engine(DatabaseSettings.build_url(), echo=True)
async def get_session() -> AsyncSession:
    async_session_factory = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session_factory() as session:
        yield session