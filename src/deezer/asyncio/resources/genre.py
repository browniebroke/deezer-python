from __future__ import annotations

from .resource import AsyncResource


class AsyncGenre(AsyncResource):
    """Async genre resource."""

    id: int
    name: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str

    async def get_artists(self, **kwargs) -> list:
        """Get all artists for a genre."""
        return await self.get_relation("artists", **kwargs)

    async def get_podcasts(self, **kwargs) -> list:
        """Get all podcasts for a genre."""
        return await self.get_relation("podcasts", **kwargs)

    async def get_radios(self, **kwargs) -> list:
        """Get all radios for a genre."""
        return await self.get_relation("radios", **kwargs)
