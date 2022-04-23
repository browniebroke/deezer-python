from __future__ import annotations

from typing import TYPE_CHECKING

from .resource import Resource

if TYPE_CHECKING:
    from ..pagination import PaginatedList
    from .track import Track
    from .user import User


class Playlist(Resource):
    """
    To work with Deezer playlist objects.

    Check the :deezer-api:`Deezer documentation <playlist>`
    for more details about each field.
    """

    id: int
    title: str
    description: str
    duration: int
    public: bool
    is_loved_track: bool
    collaborative: bool
    nb_tracks: int
    unseen_track_count: int
    fans: int
    link: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    checksum: str
    creator: User
    tracks: list[Track]

    def get_tracks(self, **kwargs) -> PaginatedList[Track]:
        """
        Get tracks from a playlist.

        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Track <deezer.resources.Track>` instances
        """
        return self.get_paginated_list("tracks", **kwargs)

    def get_fans(self, **kwargs) -> PaginatedList[User]:
        """
        Get fans from a playlist.

        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`User <deezer.resources.User>` instances
        """
        return self.get_paginated_list("fans", **kwargs)
