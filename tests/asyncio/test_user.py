from __future__ import annotations

import pytest
import pytest_asyncio

from deezer.asyncio import AsyncPaginatedList, AsyncUser

pytestmark = pytest.mark.vcr


class TestAsyncUser:
    @pytest_asyncio.fixture()
    async def user(self, async_client):
        return AsyncUser(
            async_client,
            json={"id": 359622, "type": "user"},
        )

    @pytest_asyncio.fixture()
    async def current_user(self, async_client_token):
        return AsyncUser(
            async_client_token,
            json={"id": "me", "type": "user"},
        )

    @pytest.mark.asyncio
    async def test_get_albums(self, user):
        albums = user.get_albums()
        assert isinstance(albums, AsyncPaginatedList)
        albums_list = await albums.collect()
        assert len(albums_list) > 0

    @pytest.mark.asyncio
    async def test_get_artists(self, user):
        artists = user.get_artists()
        assert isinstance(artists, AsyncPaginatedList)
        artists_list = await artists.collect()
        assert len(artists_list) > 0

    @pytest.mark.asyncio
    async def test_get_tracks(self, user):
        tracks = user.get_tracks()
        assert isinstance(tracks, AsyncPaginatedList)
        tracks_list = await tracks.collect()
        assert len(tracks_list) > 0

    @pytest.mark.asyncio
    async def test_get_followers(self, user):
        followers = user.get_followers()
        assert isinstance(followers, AsyncPaginatedList)
        followers_list = await followers.collect()
        assert len(followers_list) > 0

    @pytest.mark.asyncio
    async def test_get_followings(self, user):
        followings = user.get_followings()
        assert isinstance(followings, AsyncPaginatedList)
        followings_list = await followings.collect()
        assert len(followings_list) > 0

    @pytest.mark.asyncio
    async def test_get_playlists(self, user):
        playlists = user.get_playlists()
        assert isinstance(playlists, AsyncPaginatedList)
        playlists_list = await playlists.collect()
        assert len(playlists_list) > 0

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_add_album(self, user, async_client_token):
        user.client = async_client_token
        result = await user.add_album(302127)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_remove_album(self, user, async_client_token):
        user.client = async_client_token
        result = await user.remove_album(302127)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_add_track(self, current_user):
        result = await current_user.add_track(3135556)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_remove_track(self, current_user):
        result = await current_user.remove_track(3135556)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_add_artist(self, current_user):
        result = await current_user.add_artist(27)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_remove_artist(self, current_user):
        result = await current_user.remove_artist(27)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_follow(self, current_user):
        result = await current_user.follow(315641)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_unfollow(self, current_user):
        result = await current_user.unfollow(315641)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_add_playlist(self, current_user):
        result = await current_user.add_playlist(3110421322)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_remove_playlist(self, current_user):
        result = await current_user.remove_playlist(3110421322)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_create_playlist(self, current_user):
        playlist_id = await current_user.create_playlist("My Awesome Playlist")
        assert isinstance(playlist_id, int)
