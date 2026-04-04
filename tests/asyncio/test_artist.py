from __future__ import annotations

import pytest
import pytest_asyncio

from deezer.asyncio import AsyncAlbum, AsyncArtist

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
        assert isinstance(albums, list)
        assert len(albums) > 0
        assert isinstance(albums[0], AsyncAlbum)

    @pytest.mark.asyncio
    async def test_get_top(self, daft_punk):
        tracks = await daft_punk.get_top()
        assert isinstance(tracks, list)
        assert len(tracks) > 0

    @pytest.mark.asyncio
    async def test_get_radio(self, daft_punk):
        tracks = await daft_punk.get_radio()
        assert isinstance(tracks, list)
        assert len(tracks) > 0

    @pytest.mark.asyncio
    async def test_get_related(self, daft_punk):
        related = await daft_punk.get_related()
        assert isinstance(related, list)
        assert len(related) > 0
        assert isinstance(related[0], AsyncArtist)

    @pytest.mark.asyncio
    async def test_get_playlists(self, daft_punk):
        playlists = await daft_punk.get_playlists()
        assert isinstance(playlists, list)
        assert len(playlists) > 0
