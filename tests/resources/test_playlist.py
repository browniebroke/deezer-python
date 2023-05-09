from __future__ import annotations

import pytest

import deezer

pytestmark = pytest.mark.vcr


class TestPlaylist:
    @pytest.fixture
    def playlist(self, client):
        return client.get_playlist(9200461)

    def test_attributes(self, playlist):
        assert playlist.title == "Lounge Soirée"

    def test_get_tracks(self, playlist):
        tracks = playlist.get_tracks()
        assert isinstance(tracks, deezer.PaginatedList)
        first_track = tracks[0]
        assert isinstance(first_track, deezer.Track)
        assert first_track.title == "Otherwise"
        assert len(tracks) == 102

    def test_get_fans(self, playlist):
        fans = playlist.get_fans()
        assert isinstance(fans, deezer.PaginatedList)
        first_fan = fans[0]
        assert isinstance(first_fan, deezer.User)
        assert first_fan.name == "Fay22"
        assert len(fans) == 100

    def test_add_tracks(self, client_token):
        playlist = client_token.get_playlist(11015569602)
        # Test that we can add one track.
        result = playlist.add_tracks([79875054])
        assert result is True
        # Test that we can add multiple tracks
        result = playlist.add_tracks([79875064, 79875044, 142986210])
        assert result is True
        # Test that we can add tracks not using id's
        track = client_token.get_track(1724605597)
        result = playlist.add_tracks([track])
        assert result is True

    def test_delete_tracks(self, client_token):
        playlist = client_token.get_playlist(11015569602)
        # Test that we can delete one track.
        result = playlist.delete_tracks([79875054])
        assert result is True
        # Test that we can delete multiple tracks
        result = playlist.delete_tracks([79875064, 79875044, 142986210])
        assert result is True
        # Test that we can add tracks not using id's
        track = client_token.get_track(1724605597)
        result = playlist.delete_tracks([track])
        assert result is True

    def test_reorder_tracks(self, client_token):
        playlist = client_token.get_playlist(11336462844)
        result = playlist.reorder_tracks([79875044, 79875050, 142986210])
        assert result is True

    def test_mark_seen(self, client_token, playlist):
        result = playlist.mark_seen()
        assert result is True
