from __future__ import annotations

import pytest

import deezer

pytestmark = pytest.mark.vcr


class TestEpisode:
    def test_get_episode(self, client):
        episode = client.get_episode(343457312)
        assert isinstance(episode, deezer.Episode)
        assert episode.title == "Stuart Hogg and the GOAT"

    def test_as_dict(self, client):
        """Test resource conversion to dict."""
        episode = client.get_episode(343457312)
        episode_dict = episode.as_dict()
        assert episode_dict["id"] == 343457312
        assert episode_dict["release_date"] == "2021-11-22 23:42:00"

    def test_access_inferable_fields(self, client):
        """Accessing a missing inferable field doesn't do any API calls."""
        episode = deezer.Episode(
            client,
            json={
                "id": 343457312,
                "type": "episode",
            },
        )
        assert episode.link == "https://www.deezer.com/episode/343457312"
        assert episode.share == (
            "https://www.deezer.com/episode/343457312?utm_source=deezer"
            "&utm_content=episode-343457312&utm_medium=web"
        )

    def test_access_non_inferable_field(self, client):
        episode = deezer.Episode(
            client,
            json={
                "id": 343457312,
                "type": "episode",
            },
        )
        assert episode.duration == 3254

    def test_add_bookmark(self, client_token):
        episode = deezer.Episode(
            client_token,
            json={
                "id": 343457312,
                "type": "episode",
            },
        )
        result = episode.add_bookmark(55)
        assert result is True

    def test_remove_bookmark(self, client_token):
        episode = deezer.Episode(
            client_token,
            json={
                "id": 343457312,
                "type": "episode",
            },
        )
        result = episode.remove_bookmark()
        assert result is True
