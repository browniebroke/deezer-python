from __future__ import annotations

import pytest
import pytest_asyncio

from deezer.asyncio import AsyncArtist, AsyncGenre

pytestmark = pytest.mark.vcr


class TestAsyncGenre:
    @pytest_asyncio.fixture()
    async def electro(self, async_client):
        return await async_client.get_genre(106)

    @pytest.mark.asyncio
    async def test_attributes(self, electro):
        assert hasattr(electro, "name")
        assert isinstance(electro, AsyncGenre)
        assert repr(electro) == "<AsyncGenre: Electro>"

    @pytest.mark.asyncio
    async def test_get_artists(self, electro):
        artists = await electro.get_artists()
        assert isinstance(artists, list)
        assert len(artists) > 0
        assert isinstance(artists[0], AsyncArtist)

    @pytest.mark.asyncio
    async def test_get_radios(self, electro):
        radios = await electro.get_radios()
        assert isinstance(radios, list)
        assert len(radios) > 0
