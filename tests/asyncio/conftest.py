import pytest_asyncio

from deezer.asyncio import AsyncClient


@pytest_asyncio.fixture()
async def async_client():
    """Create an async client for tests."""
    async with AsyncClient(
        headers={"Accept-Encoding": "identity"},
    ) as client:
        yield client
