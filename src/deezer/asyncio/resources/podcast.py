from __future__ import annotations

from .resource import AsyncResource


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

    async def get_episodes(self, **kwargs) -> list:
        """Get episodes from a podcast."""
        return await self.get_relation("episodes", **kwargs)
