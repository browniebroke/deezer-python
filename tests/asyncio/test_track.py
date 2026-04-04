from __future__ import annotations

import pytest

from deezer.asyncio import AsyncAlbum, AsyncArtist, AsyncTrack

pytestmark = pytest.mark.vcr


class TestAsyncTrack:
    @pytest.mark.asyncio
    async def test_track_attributes(self, async_client):
        track = await async_client.get_track(3135556)
        assert hasattr(track, "title")
        assert isinstance(track, AsyncTrack)
        assert repr(track) == "<AsyncTrack: Harder Better Faster Stronger>"

        artist = await track.get_artist()
        assert isinstance(artist, AsyncArtist)
        assert repr(artist) == "<AsyncArtist: Daft Punk>"

        album = await track.get_album()
        assert isinstance(album, AsyncAlbum)
        assert repr(album) == "<AsyncAlbum: Discovery>"

    @pytest.mark.asyncio
    async def test_contributors(self, async_client):
        track = await async_client.get_track(1425844092)
        contributors = track.contributors
        assert isinstance(contributors, list)
        assert len(contributors) == 2
        assert all(isinstance(c, AsyncArtist) for c in contributors)
        assert [c.id for c in contributors] == [51204222, 288166]
