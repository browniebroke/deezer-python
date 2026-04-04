from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING

from deezer.dates import parse_date

from .artist import AsyncArtist
from .resource import AsyncResource

if TYPE_CHECKING:
    from .album import AsyncAlbum


class AsyncTrack(AsyncResource):
    """Async track resource."""

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
    alternative: AsyncTrack
    contributors: list[AsyncArtist]
    md5_image: str
    artist: AsyncArtist
    album: AsyncAlbum

    _parse_release_date = staticmethod(parse_date)

    def _parse_contributors(self, raw_value):
        return [AsyncArtist(client=self.client, json=val) for val in raw_value]

    async def get_artist(self) -> AsyncArtist:
        """Get the artist of the Track."""
        return await self.client.request("GET", f"artist/{self.artist.id}")

    async def get_album(self) -> AsyncAlbum:
        """Get the album of the Track."""
        return await self.client.request("GET", f"album/{self.album.id}")
