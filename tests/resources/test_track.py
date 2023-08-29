from __future__ import annotations

import pytest

import deezer

pytestmark = pytest.mark.vcr


class TestTrack:
    def test_track_attributes(self, client):
        """Test track resource."""
        track = client.get_track(3135556)
        artist = track.get_artist()
        album = track.get_album()
        assert hasattr(track, "title")
        assert isinstance(track, deezer.Track)
        assert isinstance(artist, deezer.Artist)
        assert isinstance(album, deezer.Album)
        assert repr(track) == "<Track: Harder Better Faster Stronger>"
        assert repr(artist) == "<Artist: Daft Punk>"
        assert repr(album) == "<Album: Discovery>"

    def test_contributors(self, client):
        track = client.get_track(1425844092)
        contributors = track.contributors
        assert isinstance(contributors, list)
        assert len(contributors) == 2
        assert all(isinstance(c, deezer.Artist) for c in contributors)
        assert [c.id for c in contributors] == [51204222, 288166]
