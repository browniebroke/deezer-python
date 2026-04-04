from __future__ import annotations

from typing import TYPE_CHECKING

from .resource import AsyncResource

if TYPE_CHECKING:
    from deezer.asyncio.pagination import AsyncPaginatedList


class AsyncChart(AsyncResource):
    """Async chart resource."""

    type = "chart"

    id: int

    async def get_tracks(self, **kwargs) -> AsyncPaginatedList:
        """Return the chart for tracks."""
        return await self.get_paginated_list("tracks", **kwargs)

    async def get_albums(self, **kwargs) -> AsyncPaginatedList:
        """Return the chart for albums."""
        return await self.get_paginated_list("albums", **kwargs)

    async def get_artists(self, **kwargs) -> AsyncPaginatedList:
        """Return the chart for artists."""
        return await self.get_paginated_list("artists", **kwargs)

    async def get_playlists(self, **kwargs) -> AsyncPaginatedList:
        """Return the chart for playlists."""
        return await self.get_paginated_list("playlists", **kwargs)

    async def get_podcasts(self, **kwargs) -> AsyncPaginatedList:
        """Return the chart for podcasts."""
        return await self.get_paginated_list("podcasts", **kwargs)
