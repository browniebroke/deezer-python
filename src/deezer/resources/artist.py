from __future__ import annotations

from typing import TYPE_CHECKING

from ..pagination import PaginatedList
from .resource import Resource

if TYPE_CHECKING:
    from .album import Album
    from .playlist import Playlist
    from .track import Track


class Artist(Resource):
    """
    To work with Deezer artist objects.

    Check the :deezer-api:`Deezer documentation <artist>`
    for more details about each field.
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

    def get_top(self, **kwargs) -> PaginatedList[Track]:
        """
        Get the top tracks of an artist.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Track <deezer.Track>` instances.
        """
        return self.get_paginated_list("top", **kwargs)

    def get_related(self, **kwargs) -> PaginatedList[Artist]:
        """
        Get a list of related artists.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Artist <deezer.Artist>` instances
        """
        return self.get_paginated_list("related", **kwargs)

    def get_radio(self, **kwargs) -> list[Track]:
        """
        Get a list of tracks.

        :returns: list of :class:`Track <deezer.Track>` instances
        """
        return self.get_relation("radio", **kwargs)

    def get_albums(self, **kwargs) -> PaginatedList[Album]:
        """
        Get a list of artist's albums.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Album <deezer.Album>` instances
        """
        return self.get_paginated_list("albums", **kwargs)

    def get_playlists(self, **kwargs) -> PaginatedList[Playlist]:
        """
        Get a list of artist's playlists.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Playlist <deezer.Playlist>` instances
        """
        return self.get_paginated_list("playlists", **kwargs)
