import pytest

from src.models.product import ProductModel


@pytest.fixture
async def fake_product(async_session_on_memory):
    product = ProductModel(name="Test Product", price=9.99)
    async_session_on_memory.add(product)
    await async_session_on_memory.commit()
    await async_session_on_memory.refresh(product)
    yield product
    await async_session_on_memory.delete(product)