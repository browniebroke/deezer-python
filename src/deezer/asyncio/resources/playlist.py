from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING

from deezer.utils import gen_ids

from .resource import AsyncResource

if TYPE_CHECKING:
    from deezer.asyncio.pagination import AsyncPaginatedList


class AsyncPlaylist(AsyncResource):
    """Async playlist resource."""

    id: int
    title: str
    description: str
    duration: int
    public: bool
    is_loved_track: bool
    collaborative: bool
    nb_tracks: int
    unseen_track_count: int
    fans: int
    link: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    checksum: str

    async def get_tracks(self, **kwargs) -> AsyncPaginatedList:
        """Get tracks from a playlist."""
        return await self.get_paginated_list("tracks", **kwargs)

    async def get_fans(self, **kwargs) -> AsyncPaginatedList:
        """Get fans from a playlist."""
        return await self.get_paginated_list("fans", **kwargs)

    async def mark_seen(self) -> bool:
        """Mark the playlist as seen."""
        return await self.client.request("POST", f"playlist/{self.id}/seen")

    async def add_tracks(self, tracks: Iterable[int]) -> bool:
        """Add tracks to a playlist."""
        track_ids_str = ",".join(str(tid) for tid in gen_ids(tracks))
        return await self.client.request("POST", f"playlist/{self.id}/tracks", params={"songs": track_ids_str})

    async def delete_tracks(self, tracks: Iterable[int]) -> bool:
        """Delete tracks from a playlist."""
        track_ids_str = ",".join(map(str, gen_ids(tracks)))
        return await self.client.request("DELETE", f"playlist/{self.id}/tracks", params={"songs": track_ids_str})

    async def reorder_tracks(self, order: Iterable[int]) -> bool:
        """Reorder the tracks of a playlist."""
        order_track_ids_str = ",".join(map(str, gen_ids(order)))
        return await self.client.request("POST", f"playlist/{self.id}/tracks", params={"order": order_track_ids_str})
