from __future__ import annotations

from typing import TYPE_CHECKING

from .resource import Resource

if TYPE_CHECKING:
    from ..pagination import PaginatedList
    from .episode import Episode


class Podcast(Resource):
    """
    To work with Deezer podcast objects.

    Check the :deezer-api:`Deezer documentation <podcast>`
    for more details about each field.
    """

    id: int
    title: str
    description: str
    available: bool
    fans: int
    link: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str

    def get_episodes(self, **kwargs) -> PaginatedList[Episode]:
        """
        Get episodes from a podcast

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Episode <deezer.Episode>` instances
        """
        return self.get_paginated_list("episodes", **kwargs)
