from __future__ import annotations

from .resource import AsyncResource


class AsyncArtist(AsyncResource):
    """To work with async Deezer artist objects."""

    id: int
    name: str
    link: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    nb_album: int
    nb_fan: int
    radio: bool
    tracklist: str
