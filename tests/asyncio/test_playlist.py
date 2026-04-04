from __future__ import annotations

import pytest
import pytest_asyncio

from deezer.asyncio import AsyncPlaylist

pytestmark = pytest.mark.vcr


class TestAsyncPlaylist:
    @pytest_asyncio.fixture()
    async def playlist(self, async_client):
        return AsyncPlaylist(
            async_client,
            json={"id": 9200461, "type": "playlist"},
        )

    @pytest.mark.asyncio
    async def test_attributes(self, async_client):
        playlist = await async_client.get_playlist(9200461)
        assert isinstance(playlist, AsyncPlaylist)
        assert playlist.title == "Lounge Soirée"

    @pytest.mark.asyncio
    async def test_get_tracks(self, playlist):
        tracks = await playlist.get_tracks()
        assert isinstance(tracks, list)
        assert len(tracks) > 0

    @pytest.mark.asyncio
    async def test_get_fans(self, playlist):
        fans = await playlist.get_fans()
        assert isinstance(fans, list)
        assert len(fans) > 0

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_add_tracks(self, async_client):
        playlist = AsyncPlaylist(
            async_client,
            json={"id": 11015569602, "type": "playlist"},
        )
        result = await playlist.add_tracks([79875054])
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_delete_tracks(self, async_client):
        playlist = AsyncPlaylist(
            async_client,
            json={"id": 11015569602, "type": "playlist"},
        )
        result = await playlist.delete_tracks([79875054])
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_mark_seen(self, async_client):
        playlist = AsyncPlaylist(
            async_client,
            json={"id": 9200461, "type": "playlist"},
        )
        result = await playlist.mark_seen()
        assert result is True
