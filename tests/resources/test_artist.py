from __future__ import annotations

import pytest

import deezer

pytestmark = pytest.mark.vcr


class TestArtist:
    @pytest.fixture()
    def daft_punk(self, client):
        return client.get_artist(27)

    def test_attributes(self, daft_punk):
        assert hasattr(daft_punk, "name")
        assert isinstance(daft_punk, deezer.Artist)
        assert repr(daft_punk) == "<Artist: Daft Punk>"

    def test_get_albums(self, daft_punk):
        albums = daft_punk.get_albums()
        assert isinstance(albums, deezer.PaginatedList)
        album = albums[0]
        assert isinstance(album, deezer.Album)
        assert repr(album) == "<Album: Random Access Memories>"
        assert len(albums) == 32

    def test_get_top(self, daft_punk):
        tracks = daft_punk.get_top()
        assert isinstance(tracks, deezer.PaginatedList)
        track = tracks[0]
        assert isinstance(track, deezer.Track)
        assert repr(track) == "<Track: Instant Crush>"
        assert len(tracks) == 100

    def test_get_radio(self, daft_punk):
        tracks = daft_punk.get_radio()
        assert isinstance(tracks, list)
        assert len(tracks) == 25
        track = tracks[0]
        assert isinstance(track, deezer.Track)
        assert repr(track) == "<Track: One More Time>"

    def test_get_related(self, daft_punk):
        related_artists = daft_punk.get_related()
        assert isinstance(related_artists, deezer.PaginatedList)
        related_artist = related_artists[0]
        assert isinstance(related_artist, deezer.Artist)
        assert repr(related_artist) == "<Artist: Justice>"
        assert len(related_artists) == 39

    def test_get_playlists(self, daft_punk):
        playlists = daft_punk.get_playlists()
        assert isinstance(playlists, deezer.PaginatedList)
        playlist = playlists[0]
        assert isinstance(playlist, deezer.Playlist)
        assert repr(playlist) == "<Playlist: En mode 90>"
        assert len(playlists) == 100
