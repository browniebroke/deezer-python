from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING

from ..dates import parse_date
from .resource import Resource

if TYPE_CHECKING:
    from ..pagination import PaginatedList
    from .album import Album
    from .artist import Artist
    from .playlist import Playlist
    from .track import Track


class User(Resource):
    """
    To work with Deezer user objects.

    Check the :deezer-api:`Deezer documentation <user>`
    for more details about each field.
    """

    id: int
    name: str
    lastname: str | None
    firstname: str | None
    email: str | None
    status: int | None
    birthday: dt.date | None
    inscription_date: dt.date
    gender: str | None
    link: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    country: str
    lang: str | None
    is_kid: bool | None
    explicit_content_level: str | None
    explicit_content_levels_available: list[str] | None
    tracklist: str

    _parse_birthday = staticmethod(parse_date)
    _parse_inscription_date = staticmethod(parse_date)

    def get_albums(self, **kwargs) -> PaginatedList[Album]:
        """
        Get user's favorite albums.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Album <deezer.Album>` instances
        """
        return self.get_paginated_list("albums", **kwargs)

    def get_tracks(self, **kwargs) -> PaginatedList[Track]:
        """
        Get user's favorite tracks.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Track <deezer.Track>` instances
        """
        return self.get_paginated_list("tracks", **kwargs)

    def get_artists(self, **kwargs) -> PaginatedList[Artist]:
        """
        Get user's favorite artists.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Artist <deezer.Artist>` instances
        """
        return self.get_paginated_list("artists", **kwargs)

    def get_followers(self, **kwargs) -> PaginatedList[User]:
        """
        Get user's followers.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`User <deezer.User>` instances
        """
        return self.get_paginated_list("followers", **kwargs)

    def get_followings(self, **kwargs) -> PaginatedList[User]:
        """
        Get user's followings.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`User <deezer.User>` instances
        """
        return self.get_paginated_list("followings", **kwargs)

    def get_playlists(self, **kwargs) -> PaginatedList[Playlist]:
        """
        Get user's public playlists.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Playlist <deezer.Playlist>` instances
        """
        return self.get_paginated_list("playlists", **kwargs)
