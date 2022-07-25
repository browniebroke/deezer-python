from __future__ import annotations

import pytest

import deezer

pytestmark = pytest.mark.vcr


class TestResource:
    def test_resource_relation(self, client):
        """Test passing parent object when using get_relation."""
        album = client.get_album(302127)
        tracks = album.get_tracks()
        assert tracks[0].album is album

    def test_access_field_shallow_object(self, client):
        """Accessing a field of shallow object fetches the full object."""
        episode = deezer.Episode(
            client,
            json={
                "id": 343457312,
                "type": "episode",
            },
        )
        assert episode.link == "https://www.deezer.com/episode/343457312"

    def test_field_not_found(self, client):
        """When field is missing an attribute error is raised without API calls."""
        episode = deezer.Episode(
            client,
            json={
                "id": 343457312,
                "type": "episode",
            },
        )
        with pytest.raises(AttributeError) as exc_info:
            episode.something
        assert str(exc_info.value) == "'Episode' object has no attribute 'something'"
