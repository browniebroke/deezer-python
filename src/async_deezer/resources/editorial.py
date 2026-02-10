from __future__ import annotations

from typing import TYPE_CHECKING

from .chart import Chart
from .resource import Resource

if TYPE_CHECKING:
    from async_deezer.pagination import AsyncPaginatedList

    from .album import Album


class Editorial(Resource):
    """
    Async counterpart to :class:`deezer.resources.Editorial`.
    """

    id: int
    name: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str

    async def get_selection(self) -> list[Album]:
        """Get a list of albums selected every week by the Deezer Team."""
        return await self.get_relation("selection")

    async def get_chart(self) -> Chart:
        """Get top charts for tracks, albums, artists and playlists."""
        return await self.get_relation("charts", resource_type=Chart)

    def get_releases(self, **kwargs) -> AsyncPaginatedList[Album]:
        """Get the new releases per genre for the current country."""
        return self.get_paginated_list("releases", params=kwargs or None)
