"""
Module to implement the various types of resources that
can be found in the API.
"""
import datetime as dt
from typing import List, Optional

from deezer.dates import parse_date, parse_datetime


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

    def as_dict(self):
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

    def iter_relation(self, relation, **kwargs):
        """
        Generic method to iterate relation from any resource.

        Query the client with the object's known parameters
        and try to retrieve the provided relation type. This
        is not meant to be used directly by a client, it's more
        a helper method for the child objects.
        """
        index = 0
        while 1:
            items = self.get_relation(relation, index=index, **kwargs)
            yield from items

            if len(items) == 0:
                break
            index += len(items)


class Album(Resource):
    """
    To work with an :deezer-api:`album object <album>`.

    All the fields documented on Deezer are accessible by as class attributes.
    """

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
    genres: List["Genre"]
    label: str
    nb_tracks: int
    duration: int
    fans: int
    release_date: dt.date
    record_type: str
    available: bool
    alternative: object
    tracklist: str
    explicit_lyrics: bool
    explicit_content_lyrics: int
    explicit_content_cover: int
    contributors: List["Artist"]
    artist: "Artist"

    _parse_release_date = staticmethod(parse_date)

    def _parse_contributors(self, raw_value):
        return [Artist(client=self.client, json=val) for val in raw_value]

    def get_artist(self):
        """
        Get the artist of the Album.

        :returns: the :mod:`Artist <deezer.resources.Artist>` of the Album
        """
        return self.client.get_artist(self.artist.id)

    def get_tracks(self, **kwargs):
        """
        Get a list of album's tracks.

        :returns: list of :mod:`Track <deezer.resources.Track>` instances
        """
        return self.get_relation("tracks", **kwargs)

    def iter_tracks(self, **kwargs):
        """
        Iterate album's tracks.

        :returns: iterator of :mod:`Track <deezer.resources.Track>` instances
        """
        return self.iter_relation("tracks", **kwargs)

    def rate(self, note: int) -> bool:
        """
        Rate the album with the given note.

        :param note: rating to give.
        :return: boolean, whether the album was rated
        """
        return self.client.rate_album(album_id=self.id, note=note)


class Artist(Resource):
    """
    To access an :deezer-api:`artist object <artist>`.

    All the fields documented on Deezer are accessible by as class attributes.
    """

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

    def get_top(self, **kwargs):
        """
        Get the top tracks of an artist.

        :returns: list of :mod:`Track <deezer.resources.Track>` instances
        """
        return self.get_relation("top", **kwargs)

    def get_related(self, **kwargs):
        """
        Get a list of related artists.

        :returns: list of :mod:`Artist <deezer.resources.Artist>` instances
        """
        return self.get_relation("related", **kwargs)

    def iter_related(self, **kwargs):
        """
        Iterate related artists.

        :returns: iterator of :mod:`Artist <deezer.resources.Artist>` instances
        """
        return self.iter_relation("related", **kwargs)

    def get_radio(self, **kwargs):
        """
        :returns: list of :mod:`Track <deezer.resources.Track>` instances
        """
        return self.get_relation("radio", **kwargs)

    def get_albums(self, **kwargs):
        """
        Get a list of artist's albums.

        :returns: list of :mod:`Album <deezer.resources.Album>` instances
        """
        return self.get_relation("albums", **kwargs)

    def iter_albums(self, **kwargs):
        """
        Iterate artist's albums.

        :returns: iterator of :mod:`Album <deezer.resources.Album>` instances
        """
        return self.iter_relation("albums", **kwargs)


class Genre(Resource):
    """
    To access an :deezer-api:`genre object <genre>`.

    All the fields documented on Deezer are accessible by as class attributes.
    """

    name: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str

    def get_artists(self, **kwargs):
        """
        Get all artists for a genre.

        :returns: list of :mod:`Artist <deezer.resources.Artist>` instances
        """
        return self.get_relation("artists", **kwargs)

    def iter_artists(self, **kwargs):
        """
        Iterate artists for a genre.

        :returns: iterator of :mod:`Artist <deezer.resources.Artist>` instances
        """
        return self.iter_relation("artists", **kwargs)

    def get_radios(self, **kwargs):
        """
        Get all radios for a genre.

        :returns: list of :mod:`Radio <deezer.resources.Track>` instances
        """
        return self.get_relation("radios", **kwargs)

    def iter_radios(self, **kwargs):
        """
        Iterate radios for a genre.

        :returns: iterator of :mod:`Radio <deezer.resources.Track>` instances
        """
        return self.iter_relation("radios", **kwargs)


class Track(Resource):
    """
    To access an :deezer-api:`track object <track>`.

    All the fields documented on Deezer are accessible by as class attributes.
    """

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
    available_countries: List[str]
    alternative: "Track"
    contributors: List["Artist"]
    md5_image: str
    artist: "Artist"
    album: "Album"

    _parse_release_date = staticmethod(parse_date)

    def _parse_contributors(self, raw_value):
        return [Artist(client=self.client, json=val) for val in raw_value]

    def get_artist(self):
        """
        Get the artist of the Track.

        :returns: the :mod:`Artist <deezer.resources.Artist>` of the Album
        """
        return self.client.get_artist(self.artist.id)

    def get_album(self):
        """
        :returns: the :mod:`Album <deezer.resources.Album>` instance
        """
        return self.client.get_album(self.album.id)


class User(Resource):
    """
    To access an :deezer-api:`user object <user>`.

    All the fields documented on Deezer are accessible by as class attributes.
    """

    name: str
    lastname: Optional[str]
    firstname: Optional[str]
    email: Optional[str]
    status: Optional[int]
    birthday: Optional[dt.date]
    inscription_date: dt.date
    gender: Optional[str]
    link: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    country: str
    lang: Optional[str]
    is_kid: Optional[bool]
    explicit_content_level: Optional[str]
    explicit_content_levels_available: Optional[List[str]]
    tracklist: str

    _parse_birthday = staticmethod(parse_date)
    _parse_inscription_date = staticmethod(parse_date)

    def get_albums(self, **kwargs):
        """
        Get user's favorite albums.

        :returns: list of :mod:`Album <deezer.resources.Album>` instances
        """
        return self.client.get_user_albums(self.id)

    def iter_albums(self, **kwargs):
        """
        Iterate user's favorite albums.

        :returns: iterator of :mod:`Album <deezer.resources.Album>` instances
        """
        return self.iter_relation("albums", **kwargs)

    def get_tracks(self, **kwargs):
        """
        Get user's favorite tracks.

        :returns: list of :mod:`Track <deezer.resources.Track>` instances
        """
        return self.get_relation("tracks", **kwargs)

    def iter_tracks(self, **kwargs):
        """
        Iterate user's favorite tracks.

        :returns: iterator of :mod:`Track <deezer.resources.Track>` instances
        """
        return self.iter_relation("tracks", **kwargs)

    def get_artists(self, **kwargs):
        """
        Get user's favorite artists.

        :returns: list of :mod:`Artist <deezer.resources.Artist>` instances
        """
        return self.get_relation("artists", **kwargs)

    def iter_artists(self, **kwargs):
        """
        Iterate user's favorite artists.

        :returns: iterator of :mod:`Artist <deezer.resources.Artist>` instances
        """
        return self.iter_relation("artists", **kwargs)

    def get_playlists(self, **kwargs):
        """
        Get user's public playlists.

        :returns: list of :mod:`Playlist <deezer.resources.Playlist>` instances
        """
        return self.get_relation("playlists", **kwargs)

    def iter_playlists(self, **kwargs):
        """
        Iterate user's public playlists.

        :returns: iterator of :mod:`Playlist <deezer.resources.Playlist>` instances
        """
        return self.iter_relation("playlists", **kwargs)


class Playlist(Resource):
    """
    To access an :deezer-api:`playlist object <playlist>`.

    All the fields documented on Deezer are accessible by as class attributes.
    """

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

    def get_tracks(self, **kwargs):
        """
        Get tracks from a playlist.

        :returns: list of :mod:`Track <deezer.resources.Track>` instances
        """
        return self.get_relation("tracks", **kwargs)

    def iter_tracks(self, **kwargs):
        """
        Iterate over a playlist tracks.

        :returns: iterator of :mod:`Track <deezer.resources.Track>` instances
        """
        return self.iter_relation("tracks", **kwargs)

    def get_fans(self, **kwargs):
        """
        Get fans from a playlist.

        :returns: list of :mod:`User <deezer.resources.User>` instances
        """
        return self.get_relation("fans", **kwargs)

    def iter_fans(self, **kwargs):
        """
        Iterate over fans of a playlist.

        :returns: iterator of :mod:`User <deezer.resources.User>` instances
        """
        return self.iter_relation("fans", **kwargs)


class Radio(Resource):
    """
    To access an :deezer-api:`radio object <radio>`.

    All the fields documented on Deezer are accessible by as class attributes.
    """

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

    def get_tracks(self, **kwargs):
        """
        Get first 40 tracks in the radio

        :returns: list of :mod:`Track <deezer.resources.Track>` instances
        """
        return self.get_relation("tracks", **kwargs)

    def iter_tracks(self, **kwargs):
        """
        Iterate tracks in the radio

        :returns: iterator of :mod:`Track <deezer.resources.Track>` instances
        """
        return self.iter_relation("tracks", **kwargs)


class Chart(Resource):
    """
    To access an :deezer-api:`chart object <chart>`.

    All the fields documented on Deezer are accessible by as class attributes.
    """

    type = "chart"

    id = 0
    tracks: List["Track"]
    albums: List["Album"]
    artists: List["Artist"]
    playlists: List["Playlist"]
    podcasts: List["Podcast"]

    def get_tracks(self, **kwargs):
        """
        :returns: list of :mod:`Track <deezer.resources.Track>` instances
        """
        return self.get_relation("tracks", **kwargs)

    def iter_tracks(self, **kwargs):
        """
        Iterate tracks in the radio

        :returns: iterator of :mod:`Track <deezer.resources.Track>` instances
        """
        return self.iter_relation("tracks", **kwargs)

    def get_albums(self, **kwargs):
        """
        :returns: list of :mod:`Album <deezer.resources.Album>` instances
        """
        return self.get_relation("albums", **kwargs)

    def iter_albums(self, **kwargs):
        """
        Iterate artist's albums.

        :returns: iterator of :mod:`Album <deezer.resources.Album>` instances
        """
        return self.iter_relation("albums", **kwargs)

    def get_artists(self, **kwargs):
        """
        :returns: list of :mod:`Artist <deezer.resources.Artist>` instances
        """
        return self.get_relation("artists", **kwargs)

    def iter_artists(self, **kwargs):
        """
        Iterate artists for a genre.

        :returns: iterator of :mod:`Artist <deezer.resources.Artist>` instances
        """
        return self.iter_relation("artists", **kwargs)

    def get_playlists(self, **kwargs):
        """
        :returns: list of :mod:`Playlist <deezer.resources.Playlist>` instances
        """
        return self.get_relation("playlists", **kwargs)

    def iter_playlists(self, **kwargs):
        """
        Iterate playlist for a genre.

        :returns: iterator of :mod:`Playlist <deezer.resources.Playlist>` instances
        """
        return self.iter_relation("playlists", **kwargs)


class Podcast(Resource):
    """
    To access an :deezer-api:`podcast object <podcast>`.

    All the fields documented on Deezer are accessible by as class attributes.
    """

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

    def get_episodes(self, **kwargs):
        """
        Get episodes from a podcast

        :returns: list of :mod:`Episode <deezer.resources.Episode>` instances
        """
        return self.get_relation("episodes", **kwargs)

    def iter_episodes(self, **kwargs):
        """
        Iterate over episodes of a podcast

        :returns: list of :mod:`Episode <deezer.resources.Episode>` instances
        """
        return self.iter_relation("episodes", **kwargs)


class Episode(Resource):
    """
    To access an :deezer-api:`episode object <episode>`.

    All the fields documented on Deezer are accessible by as class attributes.
    """

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
