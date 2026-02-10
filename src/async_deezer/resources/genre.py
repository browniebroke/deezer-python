from __future__ import annotations

from typing import TYPE_CHECKING

from .resource import Resource

if TYPE_CHECKING:
    from async_deezer.pagination import AsyncPaginatedList
    from .artist import Artist
    from .podcast import Podcast
    from .radio import Radio


class Genre(Resource):
    """
    Async counterpart to :class:`deezer.resources.Genre`.
    """

    id: int
    name: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str

    async def get_artists(self, **kwargs) -> list["Artist"]:
        """Get all artists for a genre."""
        return await self.get_relation("artists", params=kwargs or None)

    def get_podcasts(self, **kwargs) -> "AsyncPaginatedList[Podcast]":
        """Get all podcasts for a genre."""
        return self.get_paginated_list("podcasts", params=kwargs or None)

    async def get_radios(self, **kwargs) -> list["Radio"]:
        """Get all radios for a genre."""
        return await self.get_relation("radios", params=kwargs or None)