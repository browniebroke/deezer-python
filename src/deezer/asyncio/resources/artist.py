from __future__ import annotations

from typing import TYPE_CHECKING

from .resource import AsyncResource

if TYPE_CHECKING:
    from deezer.asyncio.pagination import AsyncPaginatedList

    from .album import AsyncAlbum


class AsyncArtist(AsyncResource):
    """To work with async Deezer artist objects."""

    id: int
    name: str
    link: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    nb_album: int
    nb_fan: int
    radio: bool
    tracklist: str

    def get_top(self, **kwargs) -> AsyncPaginatedList:
        """Get the top tracks of an artist."""
        return self.get_paginated_list("top", **kwargs)

    def get_related(self, **kwargs) -> AsyncPaginatedList[AsyncArtist]:
        """Get a list of related artists."""
        return self.get_paginated_list("related", **kwargs)

    async def get_radio(self, **kwargs) -> list:
        """Get a list of tracks."""
        return await self.get_relation("radio", fwd_parent=False, **kwargs)

    def get_albums(self, **kwargs) -> AsyncPaginatedList[AsyncAlbum]:
        """Get a list of artist's albums."""
        return self.get_paginated_list("albums", **kwargs)

    def get_playlists(self, **kwargs) -> AsyncPaginatedList:
        """Get a list of artist's playlists."""
        return self.get_paginated_list("playlists", **kwargs)
