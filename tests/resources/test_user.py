from __future__ import annotations

import pytest

import deezer

pytestmark = pytest.mark.vcr


class TestUser:
    @pytest.fixture
    def user(self, client):
        return client.get_user(359622)

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
