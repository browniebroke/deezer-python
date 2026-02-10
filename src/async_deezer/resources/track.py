from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING

from deezer.dates import parse_date

from .artist import Artist
from .resource import Resource

if TYPE_CHECKING:
    from .album import Album


class Track(Resource):
    """
    Async counterpart to :class:`deezer.resources.Track`.
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

    async def get_artist(self) -> Artist:
        """Get the artist of the track."""
        return await self.client.get_artist(self.artist.id)

    async def get_album(self) -> Album:
        """Get the album of the track."""
        return await self.client.get_album(self.album.id)
