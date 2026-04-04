from __future__ import annotations

from typing import TYPE_CHECKING

from .chart import AsyncChart
from .resource import AsyncResource

if TYPE_CHECKING:
    from deezer.asyncio.pagination import AsyncPaginatedList


class AsyncEditorial(AsyncResource):
    """Async editorial resource."""

    id: int
    name: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str

    async def get_selection(self) -> list:
        """Get a list of albums selected every week by the Deezer Team."""
        return await self.get_relation("selection")

    async def get_chart(self):
        """Get top charts for tracks, albums, artists and playlists."""
        return await self.get_relation("charts", resource_type=AsyncChart)

    async def get_releases(self, **kwargs) -> AsyncPaginatedList:
        """Get the new releases per genre for the current country."""
        return await self.get_paginated_list("releases", **kwargs)
