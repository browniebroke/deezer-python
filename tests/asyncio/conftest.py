import pytest_asyncio
from environs import Env

from deezer.asyncio import AsyncClient

env = Env()
env.read_env()


@pytest_asyncio.fixture()
async def async_client():
    """Create an async client for tests."""
    async with AsyncClient(
        headers={"Accept-Encoding": "identity"},
    ) as client:
        yield client


@pytest_asyncio.fixture()
async def async_client_token():
    """Create an authenticated async client for tests."""
    async with AsyncClient(
        access_token=env("API_TOKEN", "dummy"),
        headers={"Accept-Encoding": "identity"},
    ) as client:
        yield client
