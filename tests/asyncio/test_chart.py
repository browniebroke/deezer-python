from __future__ import annotations

import pytest
import pytest_asyncio

from deezer.asyncio import AsyncChart

pytestmark = pytest.mark.vcr


class TestAsyncChart:
    @pytest_asyncio.fixture()
    async def chart(self, async_client):
        return await async_client.get_chart(0)

    @pytest.mark.asyncio
    async def test_get_tracks(self, chart):
        tracks = await chart.get_tracks()
        assert isinstance(tracks, list)
        assert len(tracks) > 0

    @pytest.mark.asyncio
    async def test_get_albums(self, chart):
        albums = await chart.get_albums()
        assert isinstance(albums, list)
        assert len(albums) > 0

    @pytest.mark.asyncio
    async def test_get_artists(self, chart):
        artists = await chart.get_artists()
        assert isinstance(artists, list)
        assert len(artists) > 0

    @pytest.mark.asyncio
    async def test_get_playlists(self, chart):
        playlists = await chart.get_playlists()
        assert isinstance(playlists, list)
        assert len(playlists) > 0

    @pytest.mark.asyncio
    async def test_get_podcasts(self, chart):
        podcasts = await chart.get_podcasts()
        assert isinstance(podcasts, list)
        assert len(podcasts) > 0
