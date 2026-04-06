from __future__ import annotations

import pytest
import pytest_asyncio

from deezer.asyncio import AsyncAlbum, AsyncArtist, AsyncPaginatedList

pytestmark = pytest.mark.vcr


class TestAsyncArtist:
    @pytest_asyncio.fixture()
    async def daft_punk(self, async_client):
        return await async_client.get_artist(27)

    @pytest.mark.asyncio
    async def test_attributes(self, daft_punk):
        assert hasattr(daft_punk, "name")
        assert isinstance(daft_punk, AsyncArtist)
        assert repr(daft_punk) == "<AsyncArtist: Daft Punk>"

    @pytest.mark.asyncio
    async def test_get_albums(self, daft_punk):
        albums = await daft_punk.get_albums()
        assert isinstance(albums, AsyncPaginatedList)
        first = await albums.get(0)
        assert isinstance(first, AsyncAlbum)

    @pytest.mark.asyncio
    async def test_get_top(self, daft_punk):
        tracks = await daft_punk.get_top()
        assert isinstance(tracks, AsyncPaginatedList)
        first = await tracks.get(0)
        assert hasattr(first, "title")

    @pytest.mark.asyncio
    async def test_get_radio(self, daft_punk):
        tracks = await daft_punk.get_radio()
        assert isinstance(tracks, list)
        assert len(tracks) > 0

    @pytest.mark.asyncio
    async def test_get_related(self, daft_punk):
        related = await daft_punk.get_related()
        assert isinstance(related, AsyncPaginatedList)
        first = await related.get(0)
        assert isinstance(first, AsyncArtist)

    @pytest.mark.asyncio
    async def test_get_playlists(self, daft_punk):
        playlists = await daft_punk.get_playlists()
        assert isinstance(playlists, AsyncPaginatedList)
        first = await playlists.get(0)
        assert hasattr(first, "title")
