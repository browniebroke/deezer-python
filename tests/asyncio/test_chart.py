from __future__ import annotations

import pytest
import pytest_asyncio

from deezer.asyncio import AsyncPaginatedList

pytestmark = pytest.mark.vcr


class TestAsyncChart:
    @pytest_asyncio.fixture()
    async def chart(self, async_client):
        return await async_client.get_chart(0)

    @pytest.mark.asyncio
    async def test_get_tracks(self, chart):
        tracks = chart.get_tracks()
        assert isinstance(tracks, AsyncPaginatedList)
        tracks_list = await tracks.collect()
        assert len(tracks_list) > 0

    @pytest.mark.asyncio
    async def test_get_albums(self, chart):
        albums = chart.get_albums()
        assert isinstance(albums, AsyncPaginatedList)
        albums_list = await albums.collect()
        assert len(albums_list) > 0

    @pytest.mark.asyncio
    async def test_get_artists(self, chart):
        artists = chart.get_artists()
        assert isinstance(artists, AsyncPaginatedList)
        artists_list = await artists.collect()
        assert len(artists_list) > 0

    @pytest.mark.asyncio
    async def test_get_playlists(self, chart):
        playlists = chart.get_playlists()
        assert isinstance(playlists, AsyncPaginatedList)
        playlists_list = await playlists.collect()
        assert len(playlists_list) > 0

    @pytest.mark.asyncio
    async def test_get_podcasts(self, chart):
        podcasts = chart.get_podcasts()
        assert isinstance(podcasts, AsyncPaginatedList)
        podcasts_list = await podcasts.collect()
        assert len(podcasts_list) > 0
