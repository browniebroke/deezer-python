from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING, Any

from ..dates import parse_datetime
from .resource import Resource

if TYPE_CHECKING:
    from .podcast import Podcast


class Episode(Resource):
    """
    To work with Deezer episode objects.

    Check the :deezer-api:`Deezer documentation <episode>`
    for more details about each field.
    """

    id: int
    title: str
    description: str
    available: bool
    release_date: dt.datetime
    duration: int
    link: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    podcast: Podcast

    _parse_release_date = staticmethod(parse_datetime)

    def _infer_missing_field(self, item) -> Any:
        if item == "link":
            return f"https://www.deezer.com/episode/{self.id}"
        elif item == "share":
            return f"{self.link}?utm_source=deezer&utm_content=episode-{self.id}&utm_medium=web"
        return super()._infer_missing_field(item)

    def add_bookmark(self, offset: int, **kwargs) -> bool:
        """
        Sets a bookmark on the episode.

        :param offset: The offset where the bookmark is set, must be between 0 and 100.
        :returns: a boolean that tells if the operation was successful
        """
        return self.client.request(
            "POST",
            f"episode/{self.id}/bookmark",
            offset=offset,
            **kwargs,
        )

    def remove_bookmark(self, **kwargs) -> bool:
        """
        Removes the bookmark on the episode.

        :returns: a boolean that tells if the operation was successful
        """
        return self.client.request("DELETE", f"episode/{self.id}/bookmark", **kwargs)
