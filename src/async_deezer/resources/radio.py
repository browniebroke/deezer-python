from __future__ import annotations

from typing import TYPE_CHECKING

from .resource import Resource

if TYPE_CHECKING:
    from .track import Track


class Radio(Resource):
    """
    Async counterpart to :class:`deezer.resources.Radio`.
    """

    id: int
    title: str
    description: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    tracklist: str
    md5_image: str

    async def get_tracks(self) -> list["Track"]:
        """
        Get first 40 tracks in the radio. This endpoint is not paginated.
        """
        return await self.get_relation("tracks")