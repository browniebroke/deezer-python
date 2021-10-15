"""
Implements a client class to query the
`Deezer API <https://developers.deezer.com/api>`_
"""
from typing import List, Optional

import requests

from deezer.exceptions import DeezerErrorResponse, DeezerHTTPError
from deezer.resources import (
    Album,
    Artist,
    Chart,
    Comment,
    Episode,
    Genre,
    Playlist,
    Podcast,
    Radio,
    Resource,
    Track,
    User,
)


class Client:
    """
    A client to retrieve some basic infos about Deezer resourses.

    Create a client instance with the provided options. Options should
    be passed in to the constructor as kwargs.

        >>> import deezer
        >>> client = deezer.Client(app_id='foo', app_secret='bar')

    This client provides several method to retrieve the content of most
    sort of Deezer objects, based on their json structure.

    Headers can be forced by using the ``headers`` kwarg.
    For example, use ``Accept-Language`` header to force the output language.

        >>> import deezer
        >>> client = deezer.Client(headers={'Accept-Language': 'fr'})

    :param app_id: appliication ID.
    :param app_secret: application secret.
    :param access_token: user access token.
    :param headers: a dictionary of headers to be used.
    """

    objects_types = {
        "album": Album,
        "artist": Artist,
        "chart": Chart,
        "comment": Comment,
        "editorial": None,
        "episode": Episode,
        # 'folder': None, # need identification
        "genre": Genre,
        "playlist": Playlist,
        "podcast": Podcast,
        "radio": Radio,
        "search": None,
        "track": Track,
        "user": User,
    }
    base_url = "https://api.deezer.com"

    def __init__(
        self, app_id=None, app_secret=None, access_token=None, headers=None, **kwargs
    ):
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = access_token
        self.session = requests.Session()

        # Headers
        if headers:
            self.session.headers.update(headers)

    def _process_json(self, item, parent=None):
        """
        Recursively convert dictionary
        to :class:`~deezer.resources.Resource` object

        :returns: instance of :class:`~deezer.resources.Resource`
        """
        if "data" in item:
            return [self._process_json(i, parent) for i in item["data"]]

        result = {}
        for key, value in item.items():
            if isinstance(value, dict) and ("type" in value or "data" in value):
                value = self._process_json(value, parent)
            result[key] = value
        if parent is not None and hasattr(parent, "type"):
            result[parent.type] = parent

        if "type" in result:
            if result["type"] in self.objects_types:
                object_class = self.objects_types[result["type"]]
            else:
                # in case any new types are introduced by the API
                object_class = Resource
        else:
            object_class = self.objects_types[parent]
        return object_class(self, result)

    @staticmethod
    def url(request_path=""):
        """Build the url with the appended request if provided."""
        return f"https://api.deezer.com/{request_path}"

    def object_url(self, object_t, object_id=None, relation=None):
        """
        Helper method to build the url to query to access the object
        passed as parameter

        :raises TypeError: if the object type is invalid
        """
        if object_t not in self.objects_types:
            raise TypeError(f"{object_t} is not a valid type")
        request_items = (
            str(item) for item in [object_t, object_id, relation] if item is not None
        )
        request_path = "/".join(request_items)
        return self.url(request_path)

    def request(self, method: str, path: str, **params):
        """
        Make a request to the API and parse the response.

        :param method: HTTP verb to use: GET, POST< DELETE, ...
        :param path: The path to make the API call to (e.g. 'artist/1234')
        :param params: Query parameters to add the the request
        :return:
        """
        if self.access_token is not None:
            params["access_token"] = str(self.access_token)
        response = self.session.request(
            method,
            f"{self.base_url}/{path}",
            params=params,
        )
        try:
            response.raise_for_status()
        except requests.HTTPError as exc:
            raise DeezerHTTPError.from_http_error(exc) from exc
        json_data = response.json()
        if not isinstance(json_data, dict):
            return json_data
        if "error" in json_data:
            raise DeezerErrorResponse(json_data)
        return self._process_json(json_data)

    def get_object(
        self, object_t, object_id=None, relation=None, parent=None, **params
    ):
        """
        Actually query the Deezer API to retrieve the object.

        :returns: an :class:`~deezer.resources.Resource` or subclass.
        """
        url = self.object_url(object_t, object_id, relation)
        params = params or {}
        if self.access_token is not None:
            params["access_token"] = str(self.access_token)
        response = self.session.get(url, params=params)
        json_data = response.json()
        if "error" in json_data:
            raise ValueError(
                f"API request return error for object: {object_t} id: {object_id}"
            )
        return self._process_json(json_data, parent)

    def get_album(self, object_id, relation=None, **kwargs):
        """
        Get the album with the provided ID.

        :returns: an :class:`~deezer.resources.Album` object
        """
        return self.get_object("album", object_id, relation=relation, **kwargs)

    def rate_album(self, album_id: str, note: int) -> bool:
        """
        Rate the album of the given ID with the given note.

        The note should be and integer between 1 and 5.

        :returns: boolean whether rating was applied
        """
        return self.request("POST", f"album/{album_id}", note=note)

    def get_artist(self, object_id, relation=None, **kwargs):
        """
        Get the artist with the provided ID.

        :returns: an :class:`~deezer.resources.Artist` object
        """
        return self.get_object("artist", object_id, relation=relation, **kwargs)

    def get_chart(self, relation=None, index=0, limit=10, **kwargs):
        """
        Get chart

        :returns: a list of :class:`~deezer.resources.Resource` objects.
        """
        return self.get_object(
            "chart", object_id="0", relation=relation, parent="chart", **kwargs
        )

    def get_comment(self, object_id):
        """
        Get the comment with the provided id

        :returns: a :class:`~deezer.resources.Comment` object
        """
        return self.get_object("comment", object_id)

    def get_episode(self, object_id):
        """
        Get the episode with the provided id

        :returns: a :class:`~deezer.resources.Episode` object
        """
        return self.get_object("episode", object_id)

    def get_genre(self, object_id):
        """
        Get the genre with the provided id

        :returns: a :class:`~deezer.resources.Genre` object
        """
        return self.get_object("genre", object_id)

    def get_genres(self):
        """
        :returns: a list of :class:`~deezer.resources.Genre` objects.
        """
        return self.get_object("genre")

    def get_playlist(self, object_id):
        """
        Get the playlist with the provided id

        :returns: a :class:`~deezer.resources.Playlist` object
        """
        return self.get_object("playlist", object_id)

    def get_podcast(self, object_id):
        """
        Get the podcast with the provided id

        :returns: a :class:`~deezer.resources.Podcast` object
        """
        return self.get_object("podcast", object_id)

    def get_radio(self, object_id=None):
        """
        Get the radio with the provided id.

        :returns: a :class:`~deezer.resources.Radio` object
        """
        return self.get_object("radio", object_id)

    def get_radios(self):
        """
        Get a list of radios.

        :returns: a list of :class:`~deezer.resources.Radio` objects
        """
        return self.get_object("radio")

    def get_radios_top(self):
        """
        Get the top radios (5 radios).

        :returns: a :class:`~deezer.resources.Radio` object
        """
        return self.get_object("radio", relation="top")

    def get_track(self, object_id):
        """
        Get the track with the provided id

        :returns: a :class:`~deezer.resources.Track` object
        """
        return self.get_object("track", object_id)

    def get_user(self, object_id):
        """
        Get the user with the provided id

        :returns: a :class:`~deezer.resources.User` object
        """
        return self.get_object("user", object_id)

    def get_user_albums(self, user_id: Optional[int] = None) -> List[Album]:
        """
        Get the favourites albums for the given user_id if provided or current user if not.

        :param user_id: the user ID to get favourites albums.
        :return: a list of :class:`~deezer.resources.Album` instances.
        """
        user_id_str = str(user_id) if user_id else "me"
        return self.request("GET", f"user/{user_id_str}/albums")

    def add_user_album(self, album_id: int) -> bool:
        """
        Add an album to the user's library

        :param album_id: the ID of the album to add.
        :return: boolean whether the operation succeeded.
        """
        return self.request("POST", "user/me/albums", album_id=album_id)

    def remove_user_album(self, album_id: int) -> bool:
        """
        Remove an album from the user's library

        :param album_id: the ID of the album to remove.
        :return: boolean whether the operation succeeded.
        """
        return self.request("DELETE", "user/me/albums", album_id=album_id)

    def get_user_artists(self, user_id: Optional[int] = None) -> List[Artist]:
        """
        Get the favourites artists for the given user_id if provided or current user if not.

        :param user_id: the user ID to get favourites artists.
        :return: a list of :class:`~deezer.resources.Artist` instances.
        """
        user_id_str = str(user_id) if user_id else "me"
        return self.request("GET", f"user/{user_id_str}/artists")

    def add_user_artist(self, artist_id: int) -> bool:
        """
        Add an artist to the user's library

        :param artist_id: the ID of the artist to add.
        :return: boolean whether the operation succeeded.
        """
        return self.request("POST", "user/me/artists", artist_id=artist_id)

    def remove_user_artist(self, artist_id: int) -> bool:
        """
        Remove an artist from the user's library

        :param artist_id: the ID of the artist to remove.
        :return: boolean whether the operation succeeded.
        """
        return self.request("DELETE", "user/me/artists", artist_id=artist_id)

    def get_user_history(self) -> List[Track]:
        """
        Returns a list of the recently played tracks for the current user.

        :return: a list of :class:`~deezer.resources.Track` instances.
        """
        return self.request("GET", "user/me/history")

    def get_user_tracks(self, user_id: Optional[int] = None) -> List[Track]:
        """
        Get the favourites tracks for the given user_id if provided or current user if not.

        :param user_id: the user ID to get favourites tracks.
        :return: a list of :class:`~deezer.resources.Track` instances.
        """
        user_id_str = str(user_id) if user_id else "me"
        return self.request("GET", f"user/{user_id_str}/tracks")

    def add_user_track(self, track_id: int) -> bool:
        """
        Add a track to the user's library

        :param track_id: the ID of the track to add.
        :return: boolean whether the operation succeeded.
        """
        return self.request("POST", "user/me/tracks", track_id=track_id)

    def remove_user_track(self, track_id: int) -> bool:
        """
        Remove a track from the user's library

        :param track_id: the ID of the track to remove.
        :return: boolean whether the operation succeeded.
        """
        return self.request("DELETE", "user/me/tracks", track_id=track_id)

    def search(self, query, relation=None, index=0, limit=25, **kwargs):
        """
        Search track, album, artist or user

        :returns: a list of :class:`~deezer.resources.Resource` objects.
        """
        return self.get_object(
            "search", relation=relation, q=query, index=index, limit=limit, **kwargs
        )

    def advanced_search(self, terms, relation=None, index=0, limit=25, **kwargs):
        """
        Advanced search of track, album or artist.

        See `Search section of Deezer API
        <https://developers.deezer.com/api/search>`_ for search terms.

        :returns: a list of :class:`~deezer.resources.Resource` objects.

        >>> client.advanced_search({"artist": "Daft Punk", "album": "Homework"})
        >>> client.advanced_search(
        ...     {"artist": "Daft Punk", "album": "Homework"},
        ...     relation="track",
        ... )
        """
        if not isinstance(terms, dict):
            raise TypeError("terms must be a dict")
        # terms are sorted (for consistent tests between Python < 3.7 and >= 3.7)
        query = " ".join(sorted(f'{k}:"{v}"' for (k, v) in terms.items()))
        return self.get_object(
            "search", relation=relation, q=query, index=index, limit=limit, **kwargs
        )
