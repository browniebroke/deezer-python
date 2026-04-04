from __future__ import annotations

import pytest

from deezer.asyncio import AsyncEpisode

pytestmark = pytest.mark.vcr


class TestAsyncEpisode:
    @pytest.mark.asyncio
    async def test_get_episode(self, async_client):
        episode = await async_client.get_episode(343457312)
        assert isinstance(episode, AsyncEpisode)
        assert episode.title == "Stuart Hogg and the GOAT"

    @pytest.mark.asyncio
    async def test_as_dict(self, async_client):
        episode = await async_client.get_episode(343457312)
        episode_dict = episode.as_dict()
        assert episode_dict["id"] == 343457312
        assert episode_dict["release_date"] == "2021-11-22 23:42:00"

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_add_bookmark(self, async_client):
        episode = AsyncEpisode(
            async_client,
            json={"id": 343457312, "type": "episode"},
        )
        result = await episode.add_bookmark(55)
        assert result is True

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_remove_bookmark(self, async_client):
        episode = AsyncEpisode(
            async_client,
            json={"id": 343457312, "type": "episode"},
        )
        result = await episode.remove_bookmark()
        assert result is True
