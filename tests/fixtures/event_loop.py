import asyncio

import pytest

import pytest_asyncio

@pytest.fixture(scope="session")
def event_loop():
    """Override default event loop to use session scope."""
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()