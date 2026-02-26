from __future__ import annotations

from typing import TYPE_CHECKING

from .resource import Resource

if TYPE_CHECKING:
    from async_deezer.pagination import AsyncPaginatedList

    from .album import Album
    from .artist import Artist
    from .playlist import Playlist
    from .podcast import Podcast
    from .track import Track


class Chart(Resource):
    """
    Async counterpart to :class:`deezer.resources.Chart`.
    """

    type = "chart"

    id: int
    tracks: list[Track]
    albums: list[Album]
    artists: list[Artist]
    playlists: list[Playlist]
    podcasts: list[Podcast]

    def get_tracks(self, **kwargs) -> AsyncPaginatedList[Track]:
        return self.get_paginated_list("tracks", params=kwargs or None)

    def get_albums(self, **kwargs) -> AsyncPaginatedList[Album]:
        return self.get_paginated_list("albums", params=kwargs or None)

    def get_artists(self, **kwargs) -> AsyncPaginatedList[Artist]:
        return self.get_paginated_list("artists", params=kwargs or None)

    def get_playlists(self, **kwargs) -> AsyncPaginatedList[Playlist]:
        return self.get_paginated_list("playlists", params=kwargs or None)

    def get_podcasts(self, **kwargs) -> AsyncPaginatedList[Podcast]:
        return self.get_paginated_list("podcasts", params=kwargs or None)
