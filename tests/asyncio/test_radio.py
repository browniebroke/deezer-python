from __future__ import annotations

import pytest

from deezer.asyncio import AsyncRadio

pytestmark = pytest.mark.vcr


class TestAsyncRadio:
    @pytest.mark.asyncio
    async def test_attributes(self, async_client):
        radio = await async_client.get_radio(23261)
        assert isinstance(radio, AsyncRadio)
        assert hasattr(radio, "title")

    @pytest.mark.asyncio
    async def test_get_tracks(self, async_client):
        radio = await async_client.get_radio(23261)
        tracks = await radio.get_tracks()
        assert isinstance(tracks, list)
        assert len(tracks) > 0
