from __future__ import annotations

from .resource import AsyncResource


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
        from .chart import AsyncChart

        return await self.get_relation("charts", resource_type=AsyncChart)

    async def get_releases(self, **kwargs) -> list:
        """Get the new releases per genre for the current country."""
        return await self.get_relation("releases", **kwargs)
