from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING

from deezer.dates import parse_date
from deezer.utils import get_id

from .resource import Resource

if TYPE_CHECKING:
    from async_deezer.pagination import AsyncPaginatedList

    from .album import Album
    from .artist import Artist
    from .playlist import Playlist
    from .track import Track


class User(Resource):
    """
    Async counterpart to :class:`deezer.resources.User`.
    """

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

    def get_albums(self, **params) -> AsyncPaginatedList[Album]:
        """Get user's favorite albums."""
        return self.get_paginated_list("albums", params=params or None)

    async def add_album(self, album: Album | int):
        """Add an album to user's favorite albums."""
        return await self.post_relation("albums", params={"album_id": get_id(album)})

    async def remove_album(self, album: Album | int):
        """Remove an album from user's favorite albums."""
        return await self.delete_relation("albums", params={"album_id": get_id(album)})

    def get_tracks(self, **kwargs) -> AsyncPaginatedList[Track]:
        """Get user's favorite tracks."""
        return self.get_paginated_list("tracks", params=kwargs or None)

    async def add_track(self, track: Track | int):
        """Add a track to user's favorite tracks."""
        return await self.post_relation("tracks", params={"track_id": get_id(track)})

    async def remove_track(self, track: Track | int):
        """Remove a track from user's favorite tracks."""
        return await self.delete_relation("tracks", params={"track_id": get_id(track)})

    def get_artists(self, **params) -> AsyncPaginatedList[Artist]:
        """Get user's favorite artists."""
        return self.get_paginated_list("artists", params=params or None)

    async def add_artist(self, artist: Artist | int):
        """Add an artist to user's favorite artists."""
        return await self.post_relation("artists", params={"artist_id": get_id(artist)})

    async def remove_artist(self, artist: Artist | int):
        """Remove an artist from user's favorite artists."""
        return await self.delete_relation("artists", params={"artist_id": get_id(artist)})

    def get_followers(self, **params) -> AsyncPaginatedList[User]:
        """Get user's followers."""
        return self.get_paginated_list("followers", params=params or None)

    def get_followings(self, **params) -> AsyncPaginatedList[User]:
        """Get user's followings."""
        return self.get_paginated_list("followings", params=params or None)

    async def follow(self, user: User | int):
        """Follow a user."""
        return await self.post_relation("followings", params={"user_id": get_id(user)})

    async def unfollow(self, user: User | int):
        """Unfollow a user."""
        return await self.delete_relation("followings", params={"user_id": get_id(user)})

    def get_playlists(self, **params) -> AsyncPaginatedList[Playlist]:
        """Get user's public playlists."""
        return self.get_paginated_list("playlists", params=params or None)

    async def add_playlist(self, playlist: Playlist | int):
        """Add a playlist to user's public playlists."""
        return await self.post_relation("playlists", params={"playlist_id": get_id(playlist)})

    async def remove_playlist(self, playlist: Playlist | int):
        """Remove a playlist from user's public playlists."""
        return await self.delete_relation("playlists", params={"playlist_id": get_id(playlist)})

    async def create_playlist(self, title: str) -> int:
        """Create a playlist and return its ID."""
        result = await self.post_relation("playlists", params={"title": title})
        return result.id
