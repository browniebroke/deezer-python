from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING

from deezer.dates import parse_date
from deezer.utils import get_id

from .resource import AsyncResource

if TYPE_CHECKING:
    from deezer.asyncio.pagination import AsyncPaginatedList


class AsyncUser(AsyncResource):
    """Async user resource."""

    id: int
    name: str
    lastname: str | None
    firstname: str | None
    email: str | None
    status: int | None
    birthday: dt.date | None
    inscription_date: dt.date
    gender: str | None
    link: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    country: str
    lang: str | None
    is_kid: bool | None
    explicit_content_level: str | None
    explicit_content_levels_available: list[str] | None
    tracklist: str

    _parse_birthday = staticmethod(parse_date)
    _parse_inscription_date = staticmethod(parse_date)

    async def get_albums(self, **kwargs) -> AsyncPaginatedList:
        """Get user's favorite albums."""
        return await self.get_paginated_list("albums", **kwargs)

    async def add_album(self, album) -> bool:
        """Add an album to user's favorite albums."""
        return await self.post_relation("albums", params={"album_id": get_id(album)})

    async def remove_album(self, album) -> bool:
        """Remove an album from user's favorite albums."""
        return await self.delete_relation("albums", params={"album_id": get_id(album)})

    async def get_tracks(self, **kwargs) -> AsyncPaginatedList:
        """Get user's favorite tracks."""
        return await self.get_paginated_list("tracks", **kwargs)

    async def add_track(self, track) -> bool:
        """Add a track to user's favorite tracks."""
        return await self.post_relation("tracks", params={"track_id": get_id(track)})

    async def remove_track(self, track) -> bool:
        """Remove a track from user's favorite tracks."""
        return await self.delete_relation("tracks", params={"track_id": get_id(track)})

    async def get_artists(self, **kwargs) -> AsyncPaginatedList:
        """Get user's favorite artists."""
        return await self.get_paginated_list("artists", **kwargs)

    async def add_artist(self, artist) -> bool:
        """Add an artist to user's favorite artists."""
        return await self.post_relation("artists", params={"artist_id": get_id(artist)})

    async def remove_artist(self, artist) -> bool:
        """Remove an artist from user's favorite artists."""
        return await self.delete_relation("artists", params={"artist_id": get_id(artist)})

    async def get_followers(self, **kwargs) -> AsyncPaginatedList:
        """Get user's followers."""
        return await self.get_paginated_list("followers", **kwargs)

    async def get_followings(self, **kwargs) -> AsyncPaginatedList:
        """Get user's followings."""
        return await self.get_paginated_list("followings", **kwargs)

    async def follow(self, user) -> bool:
        """Follow a user."""
        return await self.post_relation("followings", params={"user_id": get_id(user)})

    async def unfollow(self, user) -> bool:
        """Unfollow a user."""
        return await self.delete_relation("followings", params={"user_id": get_id(user)})

    async def get_playlists(self, **kwargs) -> AsyncPaginatedList:
        """Get user's public playlists."""
        return await self.get_paginated_list("playlists", **kwargs)

    async def add_playlist(self, playlist) -> bool:
        """Add a playlist to user's public playlists."""
        return await self.post_relation("playlists", params={"playlist_id": get_id(playlist)})

    async def remove_playlist(self, playlist) -> bool:
        """Remove a playlist from user's public playlists."""
        return await self.delete_relation("playlists", params={"playlist_id": get_id(playlist)})

    async def create_playlist(self, title: str) -> int:
        """Create a playlist."""
        result = await self.post_relation("playlists", params={"title": title})
        return result.id
