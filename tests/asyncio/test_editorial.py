from __future__ import annotations

import pytest
import pytest_asyncio

from deezer.asyncio import AsyncEditorial

pytestmark = pytest.mark.vcr


class TestAsyncEditorial:
    @pytest_asyncio.fixture()
    async def editorial(self, async_client):
        return await async_client.get_editorial(106)

    @pytest.mark.asyncio
    async def test_attributes(self, editorial):
        assert isinstance(editorial, AsyncEditorial)
        assert hasattr(editorial, "name")

    @pytest.mark.asyncio
    async def test_get_selection(self, editorial):
        selection = await editorial.get_selection()
        assert isinstance(selection, list)
        assert len(selection) > 0

    @pytest.mark.asyncio
    async def test_get_releases(self, editorial):
        releases = await editorial.get_releases()
        assert isinstance(releases, list)
        assert len(releases) > 0
