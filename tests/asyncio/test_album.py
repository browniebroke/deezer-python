from __future__ import annotations

import pytest

from deezer.asyncio import AsyncAlbum, AsyncArtist, AsyncPaginatedList

pytestmark = pytest.mark.vcr


class TestAsyncAlbum:
    @pytest.mark.asyncio
    async def test_get_artist(self, async_client):
        album = await async_client.get_album(302127)
        assert isinstance(album, AsyncAlbum)
        assert hasattr(album, "title")
        assert repr(album) == "<AsyncAlbum: Discovery>"

        artist = await album.get_artist()
        assert isinstance(artist, AsyncArtist)
        assert repr(artist) == "<AsyncArtist: Daft Punk>"

    @pytest.mark.asyncio
    async def test_get_tracks(self, async_client):
        album = await async_client.get_album(302127)
        tracks = album.get_tracks()
        assert isinstance(tracks, AsyncPaginatedList)
        tracks_list = await tracks.collect()
        assert len(tracks_list) == 14
        assert tracks_list[0].title == "One More Time"

    @pytest.mark.asyncio
    async def test_contributors(self, async_client):
        album = await async_client.get_album(302127)
        contributors = album.contributors
        assert isinstance(contributors, list)
        assert all(isinstance(c, AsyncArtist) for c in contributors)

    @pytest.mark.asyncio
    async def test_as_dict(self, async_client):
        album = await async_client.get_album(302127)
        album_dict = album.as_dict()
        assert album_dict["id"] == 302127
        assert album_dict["release_date"] == "2001-03-07"

    @pytest.mark.asyncio
    async def test_get_relation(self, async_client):
        """Test the generic async get_relation method."""
        album = await async_client.get_album(302127)
        tracks = await album.get_relation("tracks")
        assert isinstance(tracks, list)
        assert len(tracks) > 0
