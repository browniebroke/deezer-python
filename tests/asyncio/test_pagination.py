from __future__ import annotations

import pytest
import pytest_asyncio

from deezer.asyncio import AsyncAlbum, AsyncArtist, AsyncPaginatedList

pytestmark = pytest.mark.vcr


class TestAsyncPaginatedList:
    """Tests for the AsyncPaginatedList class."""

    @pytest_asyncio.fixture()
    async def daft_punk_albums(self, async_client):
        parent = AsyncArtist(async_client, {"id": 27, "type": "artist"})
        return await AsyncPaginatedList.create(
            client=async_client,
            parent=parent,
            base_path="artist/27/albums",
        )

    @pytest.mark.asyncio
    async def test_total(self, daft_punk_albums):
        total = await daft_punk_albums.total()
        assert total == 32
        assert await daft_punk_albums.length() == 32

    @pytest.mark.asyncio
    async def test_iterate(self, daft_punk_albums):
        iter_count = 0
        async for album in daft_punk_albums:
            assert isinstance(album, AsyncAlbum)
            iter_count += 1
        assert iter_count == 32
        # This shouldn't do another API call
        assert await daft_punk_albums.total() == 32

    @pytest.mark.asyncio
    async def test_iterator(self, daft_punk_albums):
        a1 = await daft_punk_albums.__anext__()
        a2 = await daft_punk_albums.__anext__()
        a3 = await daft_punk_albums.__anext__()

        assert a1.title == "Human After All (Remixes)"
        assert a2.title == "Random Access Memories"
        assert a3.title == "TRON: Legacy Reconfigured"

    @pytest.mark.asyncio
    async def test_iterator_cross_page(self, daft_punk_albums):
        """Test __anext__ fetches the next page when the first is exhausted."""
        for _ in range(26):
            await daft_punk_albums.__anext__()
        # We successfully got element 26 (from the second page)

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        ("index", "title"),
        [
            (4, "Alive 2007"),
            (30, "One More Time"),
        ],
    )
    async def test_get_element(self, daft_punk_albums, index, title):
        album = await daft_punk_albums.get(index)
        assert isinstance(album, AsyncAlbum)
        assert album.title == title

    @pytest.mark.asyncio
    async def test_get_element_index_error(self, daft_punk_albums):
        with pytest.raises(IndexError):
            await daft_punk_albums.get(40)

    @pytest.mark.asyncio
    async def test_get_element_negative_value(self, daft_punk_albums):
        with pytest.raises(IndexError):
            await daft_punk_albums.get(-1)

    @pytest.mark.asyncio
    async def test_collect(self, daft_punk_albums):
        all_albums = await daft_punk_albums.collect()
        assert len(all_albums) == 32
        assert all(isinstance(a, AsyncAlbum) for a in all_albums)

    @pytest.mark.asyncio
    @pytest.mark.vcr(match_on=["method", "scheme", "host", "port", "path"])
    async def test_authenticated_requests(self, async_client_token):
        paginated = await AsyncPaginatedList.create(
            client=async_client_token,
            base_path="user/me/tracks",
            params={"limit": 2},
        )
        titles = [t.title async for t in paginated]
        assert titles == [
            "Poney Pt. I",
            "Young Blood",
            "Flyover",
        ]

    @pytest.mark.asyncio
    async def test_repr_many_results(self, daft_punk_albums):
        r = repr(daft_punk_albums)
        assert r.startswith("<AsyncPaginatedList [<AsyncAlbum:")
        assert "'...'" in r

    @pytest.mark.asyncio
    async def test_repr_little_results(self, async_client):
        results = await async_client.search_artists("rouquine")
        r = repr(results)
        assert "<AsyncArtist: Rouquine>" in r
        assert "..." not in r

    @pytest.mark.asyncio
    async def test_repr_empty(self, async_client):
        results = await async_client.search_artists("something very complicated without results")
        assert repr(results) == "<AsyncPaginatedList []>"

    @pytest.mark.asyncio
    async def test_grow_returns_empty(self, async_client):
        """Test __anext__ raises StopAsyncIteration when _grow returns empty."""
        parent = AsyncArtist(async_client, {"id": 27, "type": "artist"})
        paginated = await AsyncPaginatedList.create(
            client=async_client,
            parent=parent,
            base_path="artist/27/albums",
        )
        # Consume the single item from the first page
        await paginated.__anext__()
        # Next call should try to grow but get empty data, then raise
        with pytest.raises(StopAsyncIteration):
            await paginated.__anext__()

    @pytest.mark.asyncio
    async def test_anext_stop_iteration(self, async_client):
        results = await async_client.search_artists("something very complicated without results")
        with pytest.raises(StopAsyncIteration):
            await results.__anext__()
