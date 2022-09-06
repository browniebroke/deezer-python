from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING

from ..dates import parse_date
from .artist import Artist
from .resource import Resource

if TYPE_CHECKING:
    from .album import Album


class Track(Resource):
    """
    To work with Deezer track objects.

    Check the :deezer-api:`Deezer documentation <track>`
    for more details about each field.
    """

    id: int
    readable: bool
    title: str
    title_short: str
    title_version: str
    unseen: bool
    isrc: str
    link: str
    share: str
    duration: int
    track_position: int
    disk_number: int
    rank: int
    release_date: dt.date
    explicit_lyrics: bool
    explicit_content_lyrics: int
    explicit_content_cover: int
    preview: str
    bpm: float
    gain: float
    available_countries: list[str]
    alternative: Track
    contributors: list[Artist]
    md5_image: str
    artist: Artist
    album: Album

    _parse_release_date = staticmethod(parse_date)

    def _parse_contributors(self, raw_value):
        return [Artist(client=self.client, json=val) for val in raw_value]

    def get_artist(self) -> Artist:
        """
        Get the artist of the Track.

        :returns: the :class:`Artist <deezer.Artist>` of the Album
        """
        return self.client.get_artist(self.artist.id)

    def get_album(self) -> Album:
        """
        Get the album of the Track.

        :returns: the :class:`Album <deezer.Album>` instance
        """
        return self.client.get_album(self.album.id)
