from __future__ import annotations

import pytest

import deezer

pytestmark = pytest.mark.vcr


class TestUser:
    @pytest.fixture
    def user(self, client):
        return client.get_user(359622)

    @pytest.fixture
    def current_user(self, client_token):
        return deezer.User(client_token, json={"id": "me", "type": "user"})

    def test_get_albums(self, user):
        albums = user.get_albums()
        assert isinstance(albums, deezer.PaginatedList)
        album = albums[0]
        assert isinstance(album, deezer.Album)
        assert repr(album) == "<Album: A Century Of Movie Soundtracks Vol. 2>"
        assert len(albums) == 7

    def test_get_artists(self, user):
        artists = user.get_artists()
        assert isinstance(artists, deezer.PaginatedList)
        artist = artists[0]
        assert isinstance(artist, deezer.Artist)
        assert repr(artist) == "<Artist: Wax Tailor>"
        assert len(artists) == 7

    def test_get_followers(self, user):
        users = user.get_followers()
        assert isinstance(users, deezer.PaginatedList)
        user = users[0]
        assert isinstance(user, deezer.User)
        assert repr(user) == "<User: John Doe>"
        assert len(users) == 2

    def test_get_followings(self, user):
        users = user.get_followings()
        assert isinstance(users, deezer.PaginatedList)
        user = users[0]
        assert isinstance(user, deezer.User)
        assert repr(user) == "<User: John Doe>"
        assert len(users) == 2

    def test_get_playlists(self, user):
        playlists = user.get_playlists()
        assert isinstance(playlists, deezer.PaginatedList)
        playlist = playlists[0]
        assert isinstance(playlist, deezer.Playlist)
        assert repr(playlist) == "<Playlist: AC/DC>"
        assert len(playlists) == 25

    def test_get_tracks(self, user):
        tracks = user.get_tracks()
        assert isinstance(tracks, deezer.PaginatedList)
        track = tracks[0]
        assert isinstance(track, deezer.Track)
        assert repr(track) == "<Track: Poney Pt. I>"
        assert len(tracks) == 3

    def test_add_album_by_id(self, client_token, user: deezer.User):
        user.client = client_token
        assert user.add_album(302127) is True

    def test_add_album_obj(self, client_token, user: deezer.User):
        user.client = client_token
        album = deezer.Album(client_token, json={"id": 302127, "type": "album"})
        assert user.add_album(album) is True

    def test_remove_album_by_id(self, client_token, user: deezer.User):
        user.client = client_token
        assert user.remove_album(302127) is True

    def test_remove_album_obj(self, client_token, user: deezer.User):
        user.client = client_token
        album = deezer.Album(client_token, json={"id": 302127, "type": "album"})
        assert user.remove_album(album) is True

    def test_add_track_id(self, current_user: deezer.User):
        assert current_user.add_track(3135556) is True

    def test_add_track_obj(self, current_user: deezer.User):
        track = deezer.Track(
            current_user.client,
            json={"id": 3135556, "type": "track"},
        )
        assert current_user.add_track(track) is True

    def test_remove_track_id(self, current_user: deezer.User):
        assert current_user.remove_track(3135556) is True

    def test_remove_track_obj(self, current_user: deezer.User):
        track = deezer.Track(
            current_user.client,
            json={"id": 3135556, "type": "track"},
        )
        assert current_user.remove_track(track) is True

    def test_add_artist_id(self, current_user: deezer.User):
        assert current_user.add_artist(27) is True

    def test_add_artist_obj(self, current_user: deezer.User):
        artist = deezer.Artist(
            current_user.client,
            json={"id": 27, "type": "artist"},
        )
        assert current_user.add_artist(artist) is True

    def test_remove_artist_id(self, current_user: deezer.User):
        assert current_user.remove_artist(27) is True

    def test_remove_artist_obj(self, current_user: deezer.User):
        artist = deezer.Artist(
            current_user.client,
            json={"id": 27, "type": "artist"},
        )
        assert current_user.remove_artist(artist) is True

    def test_follow_by_id_fail(self, current_user: deezer.User):
        assert current_user.follow(27) is False

    def test_follow_by_id_ok(self, current_user: deezer.User):
        assert current_user.follow(315641) is True

    def test_follow_obj(self, current_user: deezer.User):
        artist = deezer.User(
            current_user.client,
            json={"id": 315641, "type": "user"},
        )
        assert current_user.follow(artist) is True

    def test_unfollow_by_id(self, current_user: deezer.User):
        assert current_user.unfollow(315641) is True

    def test_unfollow_obj(self, current_user: deezer.User):
        user = deezer.User(
            current_user.client,
            json={"id": 315641, "type": "user"},
        )
        assert current_user.unfollow(user)

    def test_add_playlist_failed(self, current_user: deezer.User):
        assert current_user.add_playlist(908622995) is False

    def test_add_playlist_by_id(self, current_user: deezer.User):
        assert current_user.add_playlist(3110421322) is True

    def test_add_playlist_obj(self, current_user: deezer.User):
        playlist = deezer.Playlist(
            current_user.client,
            json={"id": 4460913144, "type": "playlist"},
        )
        assert current_user.add_playlist(playlist) is True

    def test_remove_playlist_by_id(self, current_user: deezer.User):
        assert current_user.remove_playlist(3110421322) is True

    def test_remove_playlist_obj(self, current_user: deezer.User):
        playlist = deezer.Playlist(
            current_user.client,
            json={"id": 4460913144, "type": "playlist"},
        )
        assert current_user.remove_playlist(playlist) is True

    def test_create_playlist(self, current_user: deezer.User):
        playlist_id = current_user.create_playlist("My Awesome Playlist")
        assert isinstance(playlist_id, int)
        playlist = current_user.client.get_playlist(playlist_id)
        assert playlist.title == "My Awesome Playlist"
        assert playlist.creator.id == 359622
