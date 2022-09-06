from __future__ import annotations

from typing import TYPE_CHECKING

from .chart import Chart
from .resource import Resource

if TYPE_CHECKING:
    from ..pagination import PaginatedList
    from .album import Album


class Editorial(Resource):
    """
    To work with Deezer editorial objects.

    Check the :deezer-api:`Deezer documentation <editorial>`
    for more details about each field.
    """

    id: int
    name: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str

    def get_selection(self, **kwargs) -> list[Album]:
        """
        Get a list of albums selected every week by the Deezer Team.

        :returns: a list of :class:`Album <deezer.Album>` instances
        """
        return self.get_relation("selection", **kwargs)

    def get_chart(self, **kwargs) -> Chart:
        """
        Get top charts for tracks, albums, artists and playlists.

        :returns: a :class:`~deezer.Chart` instance
        """
        return self.get_relation("charts", resource_type=Chart, **kwargs)

    def get_releases(self, **kwargs) -> PaginatedList[Album]:
        """
        Get the new releases per genre for the current country.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Album <deezer.Album>` instances
        """
        return self.get_paginated_list("releases", **kwargs)
