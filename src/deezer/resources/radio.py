from __future__ import annotations

from typing import TYPE_CHECKING

from .resource import Resource

if TYPE_CHECKING:
    from .track import Track


class Radio(Resource):
    """
    To work with Deezer radio objects.

    Check the :deezer-api:`Deezer documentation <radio>`
    for more details about each field.
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

    def get_tracks(self) -> list[Track]:
        """
        Get first 40 tracks in the radio.

        Note that this endpoint is NOT paginated.

        :returns: a list of :class:`Track <deezer.Track>` instances.
        """
        return self.get_relation("tracks")
