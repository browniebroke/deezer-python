from __future__ import annotations

import pytest

import deezer

pytestmark = pytest.mark.vcr


class TestAlbum:
    def test_basic(self, client):
        """Test basic Album resource."""
        album = client.get_album(302127)
        assert hasattr(album, "title")
        assert repr(album) == "<Album: Discovery>"

        artist = album.get_artist()
        assert isinstance(artist, deezer.Artist)
        assert repr(artist) == "<Artist: Daft Punk>"

    def test_get_tracks(self, client):
        album = client.get_album(302127)

        # tests pagination
        tracks = album.get_tracks()
        assert isinstance(tracks, deezer.PaginatedList)
        track = tracks[0]
        assert isinstance(track, deezer.Track)
        assert repr(track) == "<Track: One More Time>"
        assert len(tracks) == 14

    def test_contributors(self, client):
        album = client.get_album(302128)

        contributors = album.contributors
        assert isinstance(contributors, list)
        assert len(contributors) == 2
        assert all(isinstance(c, deezer.Artist) for c in contributors)
        assert [c.id for c in contributors] == [123021, 6159602]

    def test_as_dict(self, client):
        album = client.get_album(302127)
        album_dict = album.as_dict()
        assert album_dict["id"] == 302127
        assert album_dict["release_date"] == "2001-03-07"
