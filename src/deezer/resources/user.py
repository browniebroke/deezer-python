from __future__ import annotations

import datetime as dt
from typing import TYPE_CHECKING

from ..dates import parse_date
from ..utils import get_id
from .resource import Resource

if TYPE_CHECKING:
    from ..pagination import PaginatedList
    from .album import Album
    from .artist import Artist
    from .playlist import Playlist
    from .track import Track


class User(Resource):
    """
    To work with Deezer user objects.

    Check the :deezer-api:`Deezer documentation <user>`
    for more details about each field.
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

    def get_albums(self, **kwargs) -> PaginatedList[Album]:
        """
        Get user's favorite albums.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Album <deezer.Album>` instances
        """
        return self.get_paginated_list("albums", **kwargs)

    def add_album(self, album: Album | int):
        """
        Add an album to user's favorite albums.

        :param album: an :class:`~deezer.Album` instance or its ID
        :returns: a boolean that tells if the operation was successful
        """
        return self.post_relation("albums", album_id=get_id(album))

    def remove_album(self, album: Album | int):
        """
        Remove an album from user's favorite albums.

        :param album: an :class:`~deezer.Album` instance or its ID
        :returns: a boolean that tells if the operation was successful
        """
        return self.delete_relation("albums", album_id=get_id(album))

    def get_tracks(self, **kwargs) -> PaginatedList[Track]:
        """
        Get user's favorite tracks.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Track <deezer.Track>` instances
        """
        return self.get_paginated_list("tracks", **kwargs)

    def add_track(self, track: Track | int):
        """
        Add a track to user's favorite tracks.

        :param track: a :class:`~deezer.Track` instance or its ID
        :returns: a boolean that tells if the operation was successful
        """
        return self.post_relation("tracks", track_id=get_id(track))

    def remove_track(self, track: Track | int):
        """
        Remove a track from user's favorite tracks.

        :param track: a :class:`~deezer.Track` instance or its ID
        :returns: a boolean that tells if the operation was successful
        """
        return self.delete_relation("tracks", track_id=get_id(track))

    def get_artists(self, **kwargs) -> PaginatedList[Artist]:
        """
        Get user's favorite artists.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Artist <deezer.Artist>` instances
        """
        return self.get_paginated_list("artists", **kwargs)

    def add_artist(self, artist: Artist | int):
        """
        Add an artist to user's favorite artists.

        :param artist: an :class:`~deezer.Artist` instance or its ID
        :returns: a boolean that tells if the operation was successful
        """
        return self.post_relation("artists", artist_id=get_id(artist))

    def remove_artist(self, artist: Artist | int):
        """
        Remove an artist from user's favorite artists.

        :param artist: an :class:`~deezer.Artist` instance or its ID
        :returns: a boolean that tells if the operation was successful
        """
        return self.delete_relation("artists", artist_id=get_id(artist))

    def get_followers(self, **kwargs) -> PaginatedList[User]:
        """
        Get user's followers.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`User <deezer.User>` instances
        """
        return self.get_paginated_list("followers", **kwargs)

    def get_followings(self, **kwargs) -> PaginatedList[User]:
        """
        Get user's followings.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`User <deezer.User>` instances
        """
        return self.get_paginated_list("followings", **kwargs)

    def follow(self, user: User | int):
        """
        Follow a user.

        :param user: a :class:`~deezer.User` instance or its ID
        :returns: a boolean that tells if the operation was successful
        """
        return self.post_relation("followings", user_id=get_id(user))

    def unfollow(self, user: User | int):
        """
        Unfollow a user.

        :param user: a :class:`~deezer.User` instance or its ID
        :returns: a boolean that tells if the operation was successful
        """
        return self.delete_relation("followings", user_id=get_id(user))

    def get_playlists(self, **kwargs) -> PaginatedList[Playlist]:
        """
        Get user's public playlists.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Playlist <deezer.Playlist>` instances
        """
        return self.get_paginated_list("playlists", **kwargs)

    def add_playlist(self, playlist: Playlist | int):
        """
        Add a playlist to user's public playlists.

        :param playlist: a :class:`~deezer.Playlist` instance or its ID
        :returns: a boolean that tells if the operation was successful
        """
        return self.post_relation("playlists", playlist_id=get_id(playlist))

    def remove_playlist(self, playlist: Playlist | int):
        """
        Remove a playlist from user's public playlists.

        :param playlist: a :class:`~deezer.Playlist` instance or its ID
        :returns: a boolean that tells if the operation was successful
        """
        return self.delete_relation("playlists", playlist_id=get_id(playlist))

    def create_playlist(self, title: str) -> int:
        """
        Create a playlist.

        :param title: the title of the playlist
        :returns: the ID of the playlist that was created
        """
        result = self.post_relation("playlists", title=title)
        # Note: the REST API call returns a dict with just the "id" key in it,
        # so we return that instead of the full Playlist object
        return result.id
