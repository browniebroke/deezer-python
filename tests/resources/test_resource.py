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

    def test_access_non_inferable_field_simplified_objet(self, client):
        """Fetch the full object when the missing field is not inferable."""
        track = deezer.Track(
            client,
            json={
                "id": 3135556,
                "type": "track",
            },
        )
        assert track.bpm == 123.4

    def test_access_no_infinite_fetch(self, client):
        track = deezer.Track(
            client,
            json={
                "id": 3135556,
                "type": "track",
            },
        )
        # Does and API call
        assert track.title == "Harder, Better, Faster, Stronger"

        # Response cassette has been modified to simulate missing 'bpm' field
        with pytest.raises(AttributeError) as exc_info:
            track.bpm  # noqa  B018
        assert str(exc_info.value) == "'Track' object has no attribute 'bpm'"

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
            episode.something  # noqa  B018
        assert str(exc_info.value) == "'Episode' object has no attribute 'something'"
