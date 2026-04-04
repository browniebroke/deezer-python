from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING

from deezer.dates import parse_date

from .artist import AsyncArtist
from .resource import AsyncResource

if TYPE_CHECKING:
    from deezer.asyncio.pagination import AsyncPaginatedList


class AsyncAlbum(AsyncResource):
    """
    Async album resource.

    Mirrors the sync Album but with async methods for
    traversing relations.
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
    label: str
    nb_tracks: int
    duration: int
    fans: int
    release_date: dt.date
    record_type: str
    available: bool

    tracklist: str
    explicit_lyrics: bool

    explicit_content_lyrics: int
    explicit_content_cover: int
    contributors: list[AsyncArtist]

    artist: AsyncArtist

    _parse_release_date = staticmethod(parse_date)

    def _parse_contributors(self, raw_value):
        return [AsyncArtist(client=self.client, json=val) for val in raw_value]

    async def get_artist(self) -> AsyncArtist:
        """
        Get the artist of the Album.

        :returns: an :class:`AsyncArtist` object
        """
        return await self.client.request("GET", f"artist/{self.artist.id}")

    async def get_tracks(self, **kwargs) -> AsyncPaginatedList:
        """
        Get a list of album's tracks.

        :returns: an :class:`AsyncPaginatedList` of track resources.
        """
        return await self.get_paginated_list("tracks", **kwargs)
