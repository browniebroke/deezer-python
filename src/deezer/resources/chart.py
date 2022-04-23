from __future__ import annotations

from typing import TYPE_CHECKING

from .resource import Resource

if TYPE_CHECKING:
    from ..pagination import PaginatedList
    from .album import Album
    from .artist import Artist
    from .playlist import Playlist
    from .podcast import Podcast
    from .track import Track


class Chart(Resource):
    """
    To work with Deezer chart objects.

    Check the :deezer-api:`Deezer documentation <chart>`
    for more details about each field.
    """

    type = "chart"

    id: int
    tracks: list[Track]
    albums: list[Album]
    artists: list[Artist]
    playlists: list[Playlist]
    podcasts: list[Podcast]

    def get_tracks(self, **kwargs) -> PaginatedList[Track]:
        """
        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Track <deezer.resources.Track>` instances
        """
        return self.get_paginated_list("tracks", **kwargs)

    def get_albums(self, **kwargs) -> PaginatedList[Album]:
        """
        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Album <deezer.resources.Album>` instances
        """
        return self.get_paginated_list("albums", **kwargs)

    def get_artists(self, **kwargs) -> PaginatedList[Artist]:
        """
        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Artist <deezer.resources.Artist>` instances
        """
        return self.get_paginated_list("artists", **kwargs)

    def get_playlists(self, **kwargs) -> PaginatedList[Playlist]:
        """
        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Playlist <deezer.resources.Playlist>` instances
        """
        return self.get_paginated_list("playlists", **kwargs)

    def get_podcasts(self, **kwargs) -> PaginatedList[Podcast]:
        """
        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Podcast <deezer.resources.Podcast>` instances
        """
        return self.get_paginated_list("podcasts", **kwargs)
