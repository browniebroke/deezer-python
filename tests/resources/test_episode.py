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
