from __future__ import annotations

import datetime as dt
from typing import Any

from deezer.dates import parse_date, parse_datetime
from deezer.pagination import PaginatedList


class Resource:
    """
    Base class for any resource.

    It is mainly responsible for passing a reference to the client
    to this class when instantiated, and transmit the json data into
    attributes
    """

    id: int
    type: str

    _fields_parsers = {}

    def __init__(self, client, json):
        self.client = client
        for field_name in json.keys():
            parse_func = getattr(self, f"_parse_{field_name}", None)
            if callable(parse_func):
                json[field_name] = parse_func(json[field_name])
        self._fields = tuple(json.keys())
        for key in json:
            setattr(self, key, json[key])

    def __repr__(self):
        name = getattr(self, "name", None)
        title = getattr(self, "title", None)
        id_ = getattr(self, "id", None)
        return f"<{self.__class__.__name__}: {name or title or id_}>"

    def as_dict(self) -> dict[str, Any]:
        """Convert resource to dictionary."""
        result = {}
        for key in self._fields:
            value = getattr(self, key)
            if isinstance(value, list):
                value = [i.as_dict() if isinstance(i, Resource) else i for i in value]
            elif isinstance(value, Resource):
                value = value.as_dict()
            elif isinstance(value, dt.datetime):
                value = f"{value:%Y-%m-%d %H:%M:%S}"
            elif isinstance(value, dt.date):
                value = value.isoformat()
            result[key] = value
        return result

    def get_relation(self, relation, **kwargs):
        """
        Generic method to load the relation from any resource.

        Query the client with the object's known parameters
        and try to retrieve the provided relation type. This
        is not meant to be used directly by a client, it's more
        a helper method for the child objects.
        """
        return self.client.request(
            "GET",
            f"{self.type}/{self.id}/{relation}",
            parent=self,
            **kwargs,
        )

    def get_paginated_list(
        self,
        relation: str,
        **kwargs,
    ):
        return PaginatedList(
            client=self.client,
            base_path=f"{self.type}/{self.id}/{relation}",
            parent=self,
            **kwargs,
        )


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

        :returns: the :class:`Artist <deezer.resources.Artist>` of the Album
        """
        return self.client.get_artist(self.artist.id)

    def get_tracks(self, **kwargs) -> PaginatedList[Track]:
        """
        Get a list of album's tracks.

        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Track <deezer.resources.Track>`.
        """
        return self.get_paginated_list("tracks", **kwargs)

    def rate(self, note: int) -> bool:
        """
        Rate the album with the given note.

        :param note: rating to give.
        :return: boolean, whether the album was rated
        """
        return self.client.rate_album(album_id=self.id, note=note)


class Artist(Resource):
    """
    To work with Deezer artist objects.

    Check the :deezer-api:`Deezer documentation <artist>`
    for more details about each field.
    """

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

    def get_top(self, **kwargs) -> PaginatedList[Track]:
        """
        Get the top tracks of an artist.

        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Track <deezer.resources.Track>` instances.
        """
        return self.get_paginated_list("top", **kwargs)

    def get_related(self, **kwargs) -> PaginatedList[Artist]:
        """
        Get a list of related artists.

        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Artist <deezer.resources.Artist>` instances
        """
        return self.get_paginated_list("related", **kwargs)

    def get_radio(self, **kwargs) -> list[Track]:
        """
        Get a list of tracks.

        :returns: list of :class:`Track <deezer.resources.Track>` instances
        """
        return self.get_relation("radio", **kwargs)

    def get_albums(self, **kwargs) -> PaginatedList[Album]:
        """
        Get a list of artist's albums.

        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Album <deezer.resources.Album>` instances
        """
        return self.get_paginated_list("albums", **kwargs)

    def get_playlists(self, **kwargs) -> PaginatedList[Playlist]:
        """
        Get a list of artist's playlists.

        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Playlist <deezer.resources.Playlist>` instances
        """
        return self.get_paginated_list("playlists", **kwargs)


class Genre(Resource):
    """
    To work with Deezer genre objects.

    Check the :deezer-api:`Deezer documentation <genre>`
    for more details about each field.
    """

    id: int
    name: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str

    def get_artists(self, **kwargs) -> list[Artist]:
        """
        Get all artists for a genre.

        :returns: list of :class:`Artist <deezer.resources.Artist>` instances
        """
        return self.get_relation("artists", **kwargs)

    def get_podcasts(self, **kwargs) -> PaginatedList[Podcast]:
        """
        Get all podcasts for a genre.

        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Podcast <deezer.resources.Podcast>` instances
        """
        return self.get_paginated_list("podcasts", **kwargs)

    def get_radios(self, **kwargs) -> list[Radio]:
        """
        Get all radios for a genre.

        :returns: list of :class:`Radio <deezer.resources.Radio>` instances
        """
        return self.get_relation("radios", **kwargs)


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

        :returns: the :class:`Artist <deezer.resources.Artist>` of the Album
        """
        return self.client.get_artist(self.artist.id)

    def get_album(self) -> Album:
        """
        Get the album of the Track.

        :returns: the :class:`Album <deezer.resources.Album>` instance
        """
        return self.client.get_album(self.album.id)


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

        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Album <deezer.resources.Album>` instances
        """
        return self.get_paginated_list("albums", **kwargs)

    def get_tracks(self, **kwargs) -> PaginatedList[Track]:
        """
        Get user's favorite tracks.

        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Track <deezer.resources.Track>` instances
        """
        return self.get_paginated_list("tracks", **kwargs)

    def get_artists(self, **kwargs) -> PaginatedList[Artist]:
        """
        Get user's favorite artists.

        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Artist <deezer.resources.Artist>` instances
        """
        return self.get_paginated_list("artists", **kwargs)

    def get_playlists(self, **kwargs) -> PaginatedList[Playlist]:
        """
        Get user's public playlists.

        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Playlist <deezer.resources.Playlist>` instances
        """
        return self.get_paginated_list("playlists", **kwargs)


class Playlist(Resource):
    """
    To work with Deezer playlist objects.

    Check the :deezer-api:`Deezer documentation <playlist>`
    for more details about each field.
    """

    id: int
    title: str
    description: str
    duration: int
    public: bool
    is_loved_track: bool
    collaborative: bool
    nb_tracks: int
    unseen_track_count: int
    fans: int
    link: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    checksum: str
    creator: User
    tracks: list[Track]

    def get_tracks(self, **kwargs) -> PaginatedList[Track]:
        """
        Get tracks from a playlist.

        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Track <deezer.resources.Track>` instances
        """
        return self.get_paginated_list("tracks", **kwargs)

    def get_fans(self, **kwargs) -> PaginatedList[User]:
        """
        Get fans from a playlist.

        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`User <deezer.resources.User>` instances
        """
        return self.get_paginated_list("fans", **kwargs)


class Radio(Resource):
    """
    To work with Deezer radio objects.

    Check the :deezer-api:`Deezer documentation <radio>`
    for more details about each field.
    """

    id: int
    title: str
    description: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    tracklist: str
    md5_image: str

    def get_tracks(self) -> list[Track]:
        """
        Get first 40 tracks in the radio.

        Note that this endpoint is NOT paginated.

        :returns: a list of :class:`Track <deezer.resources.Track>` instances.
        """
        return self.get_relation("tracks")


class Chart(Resource):
    """
    To work with Deezer chart objects.

    Check the :deezer-api:`Deezer documentation <chart>`
    for more details about each field.
    """

    type = "chart"

    id = 0
    tracks: list[Track]
    albums: list[Album]
    artists: list[Artist]
    playlists: list[Playlist]
    podcasts: list[Podcast]

    def get_tracks(self, **kwargs) -> PaginatedList[Track]:
        """
        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Track <deezer.resources.Track>` instances
        """
        return self.get_paginated_list("tracks", **kwargs)

    def get_albums(self, **kwargs) -> PaginatedList[Album]:
        """
        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Album <deezer.resources.Album>` instances
        """
        return self.get_paginated_list("albums", **kwargs)

    def get_artists(self, **kwargs) -> PaginatedList[Artist]:
        """
        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Artist <deezer.resources.Artist>` instances
        """
        return self.get_paginated_list("artists", **kwargs)

    def get_playlists(self, **kwargs) -> PaginatedList[Playlist]:
        """
        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Playlist <deezer.resources.Playlist>` instances
        """
        return self.get_paginated_list("playlists", **kwargs)

    def get_podcasts(self, **kwargs) -> PaginatedList[Podcast]:
        """
        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Podcast <deezer.resources.Podcast>` instances
        """
        return self.get_paginated_list("podcasts", **kwargs)


class Podcast(Resource):
    """
    To work with Deezer podcast objects.

    Check the :deezer-api:`Deezer documentation <podcast>`
    for more details about each field.
    """

    id: int
    title: str
    description: str
    available: bool
    fans: int
    link: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str

    def get_episodes(self, **kwargs) -> PaginatedList[Episode]:
        """
        Get episodes from a podcast

        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Episode <deezer.resources.Episode>` instances
        """
        return self.get_paginated_list("episodes", **kwargs)


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


class Editorial(Resource):
    """
    To work with Deezer editorial objects.

    Check the :deezer-api:`Deezer documentation <editorial>`
    for more details about each field.
    """

    id: int
    name: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str

    def get_selection(self, **kwargs) -> list[Album]:
        """
        Get a list of albums selected every week by the Deezer Team.

        :returns: a list of :class:`Album <deezer.resources.Album>` instances
        """
        return self.get_relation("selection", **kwargs)

    def get_chart(self, **kwargs) -> Chart:
        """
        Get top charts for tracks, albums, artists and playlists.

        :returns: a :class:`~deezer.resources.Chart` instance
        """
        return self.get_relation("charts", resource_type=Chart, **kwargs)

    def get_releases(self, **kwargs) -> PaginatedList[Album]:
        """
        Get the new releases per genre for the current country.

        :returns: a :class:`PaginatedList <deezer.pagination.PaginatedList>`
                  of :class:`Album <deezer.resources.Album>` instances
        """
        return self.get_paginated_list("releases", **kwargs)
