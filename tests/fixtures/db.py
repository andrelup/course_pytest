import pytest

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel


from src.main import app
from src.db.async_session import get_session


@pytest.fixture(scope="session")
async def async_engine_on_memory():
    engine = create_async_engine("sqlite+aiosqlite:///:memory:", 
                                connect_args={"check_same_thread": False},
                                echo=True)
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield engine
    await engine.dispose()



@pytest.fixture
async def async_session_on_memory(async_engine_on_memory):
    session_factory = sessionmaker(
            bind=async_engine_on_memory, 
            class_=AsyncSession, 
            expire_on_commit=False,
            autocommit=False,
            autoflush=False
        )
    async_session = session_factory()

    async def override_get_session():
        yield async_session
    
    app.dependency_overrides[get_session] = override_get_session