from __future__ import annotations

from typing import TYPE_CHECKING

from .resource import AsyncResource

if TYPE_CHECKING:
    from deezer.asyncio.pagination import AsyncPaginatedList


class AsyncPodcast(AsyncResource):
    """Async podcast resource."""

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

    def get_episodes(self, **kwargs) -> AsyncPaginatedList:
        """Get episodes from a podcast."""
        return self.get_paginated_list("episodes", **kwargs)
