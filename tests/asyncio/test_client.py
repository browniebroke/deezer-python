from __future__ import annotations

import pytest

from deezer.asyncio import (
    AsyncAlbum,
    AsyncArtist,
    AsyncClient,
    AsyncPaginatedList,
)
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

    @pytest.mark.asyncio
    async def test_list_editorials(self, async_client):
        editorials = async_client.list_editorials()
        assert isinstance(editorials, AsyncPaginatedList)
        first = await editorials.get(0)
        assert hasattr(first, "name")

    @pytest.mark.asyncio
    async def test_list_genres(self, async_client):
        genres = await async_client.list_genres()
        assert isinstance(genres, list)
        assert len(genres) == 23

    @pytest.mark.asyncio
    async def test_list_radios(self, async_client):
        radios = await async_client.list_radios()
        assert isinstance(radios, list)
        assert len(radios) == 115

    @pytest.mark.asyncio
    async def test_get_radios_top(self, async_client):
        radios = async_client.get_radios_top()
        assert isinstance(radios, AsyncPaginatedList)
        first = await radios.get(0)
        assert hasattr(first, "title")

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_get_user_recommended_tracks(self, async_client_token):
        tracks = async_client_token.get_user_recommended_tracks()
        assert isinstance(tracks, AsyncPaginatedList)
        first = await tracks.get(0)
        assert hasattr(first, "title")

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_get_user_recommended_albums(self, async_client_token):
        albums = async_client_token.get_user_recommended_albums()
        assert isinstance(albums, AsyncPaginatedList)
        first = await albums.get(0)
        assert hasattr(first, "title")

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_get_user_recommended_artists(self, async_client_token):
        artists = async_client_token.get_user_recommended_artists()
        assert isinstance(artists, AsyncPaginatedList)
        first = await artists.get(0)
        assert hasattr(first, "name")

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_get_user_recommended_playlists(self, async_client_token):
        playlists = async_client_token.get_user_recommended_playlists()
        assert isinstance(playlists, AsyncPaginatedList)
        first = await playlists.get(0)
        assert hasattr(first, "title")

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_get_user_flow(self, async_client_token):
        flow = async_client_token.get_user_flow()
        assert isinstance(flow, AsyncPaginatedList)
        first = await flow.get(0)
        assert hasattr(first, "title")

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_get_user_history(self, async_client_token):
        history = async_client_token.get_user_history()
        assert isinstance(history, AsyncPaginatedList)
        first = await history.get(0)
        assert hasattr(first, "title")

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_add_user_album(self, async_client_token):
        result = await async_client_token.add_user_album(302127)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_remove_user_album(self, async_client_token):
        result = await async_client_token.remove_user_album(302127)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_add_user_artist(self, async_client_token):
        result = await async_client_token.add_user_artist(243)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_remove_user_artist(self, async_client_token):
        result = await async_client_token.remove_user_artist(243)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_add_user_following(self, async_client_token):
        result = await async_client_token.add_user_following(2640689)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_remove_user_following(self, async_client_token):
        result = await async_client_token.remove_user_following(2640689)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_add_user_track(self, async_client_token):
        result = await async_client_token.add_user_track(1374789602)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_remove_user_track(self, async_client_token):
        result = await async_client_token.remove_user_track(1374789602)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_add_user_playlist(self, async_client_token):
        result = await async_client_token.add_user_playlist(8749345882)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_remove_user_playlist(self, async_client_token):
        result = await async_client_token.remove_user_playlist(8749345882)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_create_playlist(self, async_client_token):
        result = await async_client_token.create_playlist("CoolPlaylist")
        assert result == 11336219744

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_delete_playlist(self, async_client_token):
        result = await async_client_token.delete_playlist(11336219744)
        assert result is True

    @pytest.mark.asyncio
    async def test_search_simple(self, async_client):
        result = async_client.search("Soliloquy")
        assert isinstance(result, AsyncPaginatedList)
        first = await result.get(0)
        assert hasattr(first, "title")

    @pytest.mark.asyncio
    async def test_search_albums(self, async_client):
        result = async_client.search_albums("Daft Punk")
        assert isinstance(result, AsyncPaginatedList)
        first = await result.get(0)
        assert hasattr(first, "title")

    @pytest.mark.asyncio
    async def test_search_artists(self, async_client):
        result = async_client.search_artists("Daft Punk")
        assert isinstance(result, AsyncPaginatedList)
        first = await result.get(0)
        assert hasattr(first, "name")

    @pytest.mark.asyncio
    async def test_search_playlists(self, async_client):
        result = async_client.search_playlists("Daft Punk")
        assert isinstance(result, AsyncPaginatedList)
        first = await result.get(0)
        assert hasattr(first, "title")
