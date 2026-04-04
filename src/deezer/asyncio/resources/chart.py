from __future__ import annotations

from .resource import AsyncResource


class AsyncChart(AsyncResource):
    """Async chart resource."""

    type = "chart"

    id: int

    async def get_tracks(self, **kwargs) -> list:
        """Return the chart for tracks."""
        return await self.get_relation("tracks", **kwargs)

    async def get_albums(self, **kwargs) -> list:
        """Return the chart for albums."""
        return await self.get_relation("albums", **kwargs)

    async def get_artists(self, **kwargs) -> list:
        """Return the chart for artists."""
        return await self.get_relation("artists", **kwargs)

    async def get_playlists(self, **kwargs) -> list:
        """Return the chart for playlists."""
        return await self.get_relation("playlists", **kwargs)

    async def get_podcasts(self, **kwargs) -> list:
        """Return the chart for podcasts."""
        return await self.get_relation("podcasts", **kwargs)
