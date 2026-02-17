import httpx
import pytest
from fastapi.testclient import TestClient
from src.main import app


@pytest.fixture
def client():
    test_client = TestClient(app)
    yield test_client
    test_client.close()

@pytest.fixture
async def async_client():
    transport = httpx.ASGITransport(app=app)
    async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
        yield client