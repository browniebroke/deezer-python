from __future__ import annotations

import pytest

import deezer
from deezer.asyncio import AsyncAlbum, AsyncArtist, AsyncClient
from deezer.exceptions import DeezerNotFoundError

pytestmark = pytest.mark.vcr


class TestAsyncClient:
    @pytest.mark.asyncio
    async def test_get_album(self, async_client):
        album = await async_client.get_album(302127)
        assert isinstance(album, AsyncAlbum)
        assert album.title == "Discovery"
        assert repr(album) == "<AsyncAlbum: Discovery>"

    @pytest.mark.asyncio
    async def test_get_album_attributes(self, async_client):
        album = await async_client.get_album(302127)
        assert album.id == 302127
        assert album.title == "Discovery"
        assert album.nb_tracks == 14
        assert album.release_date.isoformat() == "2001-03-07"
        assert isinstance(album.artist, AsyncArtist)
        assert album.artist.name == "Daft Punk"

    @pytest.mark.asyncio
    async def test_get_album_contributors(self, async_client):
        album = await async_client.get_album(302127)
        contributors = album.contributors
        assert isinstance(contributors, list)
        assert all(isinstance(c, AsyncArtist) for c in contributors)

    @pytest.mark.asyncio
    async def test_request_not_found(self, async_client):
        with pytest.raises(DeezerNotFoundError):
            await async_client.request("GET", "album/0")

    @pytest.mark.asyncio
    async def test_as_dict(self, async_client):
        album = await async_client.get_album(302127)
        album_dict = album.as_dict()
        assert album_dict["id"] == 302127
        assert album_dict["title"] == "Discovery"
        assert album_dict["release_date"] == "2001-03-07"

    @pytest.mark.asyncio
    async def test_context_manager(self):
        async with AsyncClient(
            headers={"Accept-Encoding": "identity"},
        ) as client:
            assert isinstance(client, AsyncClient)
            album = await client.get_album(302127)
            assert album.title == "Discovery"

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_access_token(self):
        async with AsyncClient(
            access_token="dummy",
            headers={"Accept-Encoding": "identity"},
        ) as client:
            album = await client.get_album(302127)
            assert isinstance(album, AsyncAlbum)
