from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING

from deezer.dates import parse_datetime

from .resource import AsyncResource

if TYPE_CHECKING:
    from .podcast import AsyncPodcast


class AsyncEpisode(AsyncResource):
    """Async episode resource."""

    id: int
    title: str
    description: str
    available: bool
    release_date: dt.datetime
    duration: int
    link: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    podcast: AsyncPodcast

    _parse_release_date = staticmethod(parse_datetime)

    async def add_bookmark(self, offset: int) -> bool:
        """Set a bookmark on the episode."""
        return await self.client.request(
            "POST",
            f"episode/{self.id}/bookmark",
            params={"offset": offset},
        )

    async def remove_bookmark(self) -> bool:
        """Remove the bookmark on the episode."""
        return await self.client.request("DELETE", f"episode/{self.id}/bookmark")
