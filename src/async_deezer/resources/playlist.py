from __future__ import annotations

from collections.abc import Iterable
from typing import TYPE_CHECKING

from deezer.utils import gen_ids

from .resource import Resource

if TYPE_CHECKING:
    from async_deezer.pagination import AsyncPaginatedList

    from .track import Track
    from .user import User


class Playlist(Resource):
    """
    Async counterpart to :class:`deezer.resources.Playlist`.
    """

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
    creator: User
    tracks: list[Track]

    def get_tracks(self, **kwargs) -> AsyncPaginatedList[Track]:
        """Get tracks from a playlist."""
        return self.get_paginated_list("tracks", params=kwargs or None)

    def get_fans(self, **kwargs) -> AsyncPaginatedList[User]:
        """Get fans from a playlist."""
        return self.get_paginated_list("fans", params=kwargs or None)

    async def mark_seen(self) -> bool:
        """Mark the playlist as seen."""
        return await self.client.request("POST", f"playlist/{self.id}/seen")

    async def add_tracks(self, tracks: Iterable[int | Track]) -> bool:
        """Add tracks to a playlist."""
        track_ids_str = ",".join(str(tid) for tid in gen_ids(tracks))
        return await self.client.request(
            "POST",
            f"playlist/{self.id}/tracks",
            params={"songs": track_ids_str},
        )

    async def delete_tracks(self, tracks: Iterable[int | Track]) -> bool:
        """Delete tracks from a playlist."""
        track_ids_str = ",".join(map(str, gen_ids(tracks)))
        return await self.client.request(
            "DELETE",
            f"playlist/{self.id}/tracks",
            params={"songs": track_ids_str},
        )

    async def reorder_tracks(self, order: Iterable[int | Track]) -> bool:
        """Reorder the tracks of a playlist."""
        order_track_ids_str = ",".join(map(str, gen_ids(order)))
        return await self.client.request(
            "POST",
            f"playlist/{self.id}/tracks",
            params={"order": order_track_ids_str},
        )
