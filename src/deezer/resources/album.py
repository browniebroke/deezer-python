from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING

from ..dates import parse_date
from ..pagination import PaginatedList
from .artist import Artist
from .resource import Resource

if TYPE_CHECKING:
    from .genre import Genre
    from .track import Track


class Album(Resource):
    """
    To work with an album object.

    Check the :deezer-api:`Deezer documentation <album>`
    for more details about each field.
    """

    id: int
    title: str
    upc: str
    link: str
    share: str
    cover: str
    cover_small: str
    cover_medium: str
    cover_big: str
    cover_xl: str
    md5_image: str

    genre_id: int
    genres: list[Genre]
    label: str
    nb_tracks: int
    duration: int
    fans: int
    release_date: dt.date
    record_type: str
    available: bool

    alternative: Album
    tracklist: str
    explicit_lyrics: bool

    explicit_content_lyrics: int
    explicit_content_cover: int
    contributors: list[Artist]

    artist: Artist
    tracks: list[Track]

    _parse_release_date = staticmethod(parse_date)

    def _parse_contributors(self, raw_value):
        return [Artist(client=self.client, json=val) for val in raw_value]

    def get_artist(self) -> Artist:
        """
        Get the artist of the Album.

        :returns: the :class:`Artist <deezer.Artist>` of the Album
        """
        return self.client.get_artist(self.artist.id)

    def get_tracks(self, **kwargs) -> PaginatedList[Track]:
        """
        Get a list of album's tracks.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Track <deezer.Track>`.
        """
        return self.get_paginated_list("tracks", **kwargs)
