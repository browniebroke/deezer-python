from __future__ import annotations

from typing import TYPE_CHECKING

from .resource import Resource

if TYPE_CHECKING:
    from async_deezer.pagination import AsyncPaginatedList
    from .album import Album
    from .playlist import Playlist
    from .track import Track


class Artist(Resource):
    """
    Async counterpart to :class:`deezer.resources.Artist`.
    """

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

    def get_top(self, **kwargs) -> "AsyncPaginatedList[Track]":
        """Get the top tracks of an artist."""
        return self.get_paginated_list("top", params=kwargs or None)

    def get_related(self, **kwargs) -> "AsyncPaginatedList[Artist]":
        """Get a list of related artists."""
        return self.get_paginated_list("related", params=kwargs or None)

    async def get_radio(self, **kwargs) -> list["Track"]:
        """
        Get a list of tracks for the artist radio.
        """
        # radio returns tracks from different artists -> no fwd parent
        return await self.get_relation("radio", fwd_parent=False, params=kwargs or None)

    def get_albums(self, **kwargs) -> "AsyncPaginatedList[Album]":
        """Get a paginated list of artist's albums."""
        return self.get_paginated_list("albums", params=kwargs or None)

    def get_playlists(self, **kwargs) -> "AsyncPaginatedList[Playlist]":
        """Get a paginated list of artist's playlists."""
        return self.get_paginated_list("playlists", params=kwargs or None)