from __future__ import annotations

from typing import TYPE_CHECKING

from .resource import Resource

if TYPE_CHECKING:
    from ..pagination import PaginatedList
    from .artist import Artist
    from .podcast import Podcast
    from .radio import Radio


class Genre(Resource):
    """
    To work with Deezer genre objects.

    Check the :deezer-api:`Deezer documentation <genre>`
    for more details about each field.
    """

    id: int
    name: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str

    def get_artists(self, **kwargs) -> list[Artist]:
        """
        Get all artists for a genre.

        :returns: list of :class:`Artist <deezer.Artist>` instances
        """
        return self.get_relation("artists", **kwargs)

    def get_podcasts(self, **kwargs) -> PaginatedList[Podcast]:
        """
        Get all podcasts for a genre.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Podcast <deezer.Podcast>` instances
        """
        return self.get_paginated_list("podcasts", **kwargs)

    def get_radios(self, **kwargs) -> list[Radio]:
        """
        Get all radios for a genre.

        :returns: list of :class:`Radio <deezer.Radio>` instances
        """
        return self.get_relation("radios", **kwargs)
