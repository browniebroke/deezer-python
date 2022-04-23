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
