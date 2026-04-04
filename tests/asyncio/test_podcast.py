from __future__ import annotations

import pytest

from deezer.asyncio import AsyncPaginatedList, AsyncPodcast

pytestmark = pytest.mark.vcr


class TestAsyncPodcast:
    @pytest.mark.asyncio
    async def test_get_episodes(self, async_client):
        podcast = await async_client.get_podcast(699612)
        assert isinstance(podcast, AsyncPodcast)
        episodes = await podcast.get_episodes()
        assert isinstance(episodes, AsyncPaginatedList)
        episodes_list = await episodes.collect()
        assert len(episodes_list) > 0
