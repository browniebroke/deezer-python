from __future__ import annotations

import pytest
import vcr

import deezer
from deezer.asyncio import AsyncClient
from deezer.exceptions import DeezerErrorResponse, DeezerNotFoundError

my_vcr = vcr.VCR(
    cassette_library_dir="tests/asyncio/cassettes",
    filter_query_parameters=[("access_token", "dummy")],
    match_on=["method", "scheme", "host", "port", "path"],
)


class TestAsyncClient:
    @pytest.mark.asyncio
    async def test_get_album(self):
        with my_vcr.use_cassette("TestAsyncClient.test_get_album.yaml"):
            async with AsyncClient(
                headers={"Accept-Encoding": "identity"},
            ) as client:
                album = await client.get_album(302127)
                assert isinstance(album, deezer.Album)
                assert album.title == "Discovery"
                assert repr(album) == "<Album: Discovery>"

    @pytest.mark.asyncio
    async def test_get_album_attributes(self):
        with my_vcr.use_cassette("TestAsyncClient.test_get_album.yaml"):
            async with AsyncClient(
                headers={"Accept-Encoding": "identity"},
            ) as client:
                album = await client.get_album(302127)
                assert album.id == 302127
                assert album.title == "Discovery"
                assert album.nb_tracks == 14
                assert album.release_date.isoformat() == "2001-03-07"
                assert isinstance(album.artist, deezer.Artist)
                assert album.artist.name == "Daft Punk"

    @pytest.mark.asyncio
    async def test_get_album_contributors(self):
        with my_vcr.use_cassette("TestAsyncClient.test_get_album.yaml"):
            async with AsyncClient(
                headers={"Accept-Encoding": "identity"},
            ) as client:
                album = await client.get_album(302127)
                contributors = album.contributors
                assert isinstance(contributors, list)
                assert all(isinstance(c, deezer.Artist) for c in contributors)

    @pytest.mark.asyncio
    async def test_request_not_found(self):
        with my_vcr.use_cassette("TestAsyncClient.test_request_not_found.yaml"):
            async with AsyncClient(
                headers={"Accept-Encoding": "identity"},
            ) as client:
                with pytest.raises(DeezerNotFoundError):
                    await client.request("GET", "album/0")

    @pytest.mark.asyncio
    async def test_as_dict(self):
        with my_vcr.use_cassette("TestAsyncClient.test_get_album.yaml"):
            async with AsyncClient(
                headers={"Accept-Encoding": "identity"},
            ) as client:
                album = await client.get_album(302127)
                album_dict = album.as_dict()
                assert album_dict["id"] == 302127
                assert album_dict["title"] == "Discovery"
                assert album_dict["release_date"] == "2001-03-07"

    @pytest.mark.asyncio
    async def test_context_manager(self):
        with my_vcr.use_cassette("TestAsyncClient.test_get_album.yaml"):
            async with AsyncClient(
                headers={"Accept-Encoding": "identity"},
            ) as client:
                assert isinstance(client, AsyncClient)
                album = await client.get_album(302127)
                assert album.title == "Discovery"

    @pytest.mark.asyncio
    async def test_access_token(self):
        with my_vcr.use_cassette("TestAsyncClient.test_get_album.yaml"):
            async with AsyncClient(
                access_token="dummy",
                headers={"Accept-Encoding": "identity"},
            ) as client:
                album = await client.get_album(302127)
                assert isinstance(album, deezer.Album)
