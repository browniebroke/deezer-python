from __future__ import annotations

from typing import TYPE_CHECKING

from .resource import AsyncResource

if TYPE_CHECKING:
    from deezer.asyncio.pagination import AsyncPaginatedList


class AsyncChart(AsyncResource):
    """Async chart resource."""

    type = "chart"

    id: int

    def get_tracks(self, **kwargs) -> AsyncPaginatedList:
        """Return the chart for tracks."""
        return self.get_paginated_list("tracks", **kwargs)

    def get_albums(self, **kwargs) -> AsyncPaginatedList:
        """Return the chart for albums."""
        return self.get_paginated_list("albums", **kwargs)

    def get_artists(self, **kwargs) -> AsyncPaginatedList:
        """Return the chart for artists."""
        return self.get_paginated_list("artists", **kwargs)

    def get_playlists(self, **kwargs) -> AsyncPaginatedList:
        """Return the chart for playlists."""
        return self.get_paginated_list("playlists", **kwargs)

    def get_podcasts(self, **kwargs) -> AsyncPaginatedList:
        """Return the chart for podcasts."""
        return self.get_paginated_list("podcasts", **kwargs)
