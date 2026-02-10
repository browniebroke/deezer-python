from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING, Any

from deezer.dates import parse_datetime

from .resource import Resource

if TYPE_CHECKING:
    from .podcast import Podcast


class Episode(Resource):
    """
    Async counterpart to :class:`deezer.resources.Episode`.
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

    def _infer_missing_field(self, item) -> Any:  # type: ignore[override]
        if item == "link":
            return f"https://www.deezer.com/episode/{self.id}"
        elif item == "share":
            return f"{self.link}?utm_source=deezer&utm_content=episode-{self.id}&utm_medium=web"
        return super()._infer_missing_field(item)  # type: ignore[no-any-return]

    async def add_bookmark(self, offset: int) -> bool:
        """
        Sets a bookmark on the episode.
        """
        return await self.client.request(
            "POST",
            f"episode/{self.id}/bookmark",
            params={"offset": offset},
        )

    async def remove_bookmark(self) -> bool:
        """
        Removes the bookmark on the episode.
        """
        return await self.client.request("DELETE", f"episode/{self.id}/bookmark")