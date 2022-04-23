from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING

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
