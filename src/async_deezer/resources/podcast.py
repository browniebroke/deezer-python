from __future__ import annotations

from typing import TYPE_CHECKING

from .resource import Resource

if TYPE_CHECKING:
    from async_deezer.pagination import AsyncPaginatedList

    from .episode import Episode


class Podcast(Resource):
    """
    Async counterpart to :class:`deezer.resources.Podcast`.
    """

    id: int
    title: str
    description: str
    available: bool
    fans: int
    link: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str

    def get_episodes(self, **kwargs) -> AsyncPaginatedList[Episode]:
        """Get episodes from a podcast."""
        return self.get_paginated_list("episodes", params=kwargs or None)
