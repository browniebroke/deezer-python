"""
Implements a client class to query the
`Deezer API <https://developers.deezer.com/api>`_
"""
from typing import Any, Dict, List, Optional, Type, Union

import requests

from deezer.exceptions import (
    DeezerErrorResponse,
    DeezerHTTPError,
    DeezerUnknownResource,
)
from deezer.resources import (
    Album,
    Artist,
    Chart,
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

    Create a client instance with the given options. Options should
    be passed in to the constructor as kwargs.

        >>> import deezer
        >>> client = deezer.Client(app_id='foo', app_secret='bar')

    This client provides several method to retrieve the content of most
    sort of Deezer objects, based on their json structure.

    Headers can be forced by using the ``headers`` kwarg.
    For example, use ``Accept-Language`` header to force the output language.

        >>> import deezer
        >>> client = deezer.Client(headers={'Accept-Language': 'fr'})

    :param app_id: application ID.
    :param app_secret: application secret.
    :param access_token: user access token.
    :param headers: a dictionary of headers to be used.
    """

    objects_types = {
        "album": Album,
        "artist": Artist,
        "chart": Chart,
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

    def _process_json(
        self,
        item: Dict[str, Any],
        parent: Optional[Resource] = None,
        resource_type: Optional[Type[Resource]] = None,
    ):
        """
        Recursively convert dictionary
        to :class:`~deezer.resources.Resource` object

        :param item: the JSON response as dict.
        :param parent: A reference to the parent resource, to avoid fetching again.
        :param resource_type: The resource class to use as top level.
        :returns: instance of :class:`~deezer.resources.Resource`
        """
        if "data" in item:
            return [self._process_json(i, parent) for i in item["data"]]

        result = {}
        for key, value in item.items():
            if isinstance(value, dict) and ("type" in value or "data" in value):
                value = self._process_json(value, parent)
            result[key] = value
        if parent is not None:
            result[parent.type] = parent

        if "type" in result:
            if result["type"] in self.objects_types:
                object_class = self.objects_types[result["type"]]
            else:
                # in case any new types are introduced by the API
                object_class = Resource
        elif resource_type:
            object_class = resource_type
        else:
            raise DeezerUnknownResource(f"Unable to find resource type for {result!r}")
        return object_class(self, result)

    def request(
        self,
        method: str,
        path: str,
        parent: Optional[Resource] = None,
        resource_type: Optional[Type[Resource]] = None,
        **params,
    ):
        """
        Make a request to the API and parse the response.

        :param method: HTTP verb to use: GET, POST< DELETE, ...
        :param path: The path to make the API call to (e.g. 'artist/1234').
        :param parent: A reference to the parent resource, to avoid fetching again.
        :param resource_type: The resource class to use as top level.
        :param params: Query parameters to add the the request
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
        return self._process_json(json_data, parent=parent, resource_type=resource_type)

    def get_album(self, album_id: int) -> Album:
        """
        Get the album with the given ID.

        :returns: an :class:`~deezer.resources.Album` object
        """
        return self.request("GET", f"album/{album_id}")

    def rate_album(self, album_id: int, note: int) -> bool:
        """
        Rate the album of the given ID with the given note.

        The note should be and integer between 1 and 5.

        :returns: boolean whether rating was applied
        """
        return self.request("POST", f"album/{album_id}", note=note)

    def get_artist(self, artist_id: int) -> Artist:
        """
        Get the artist with the given ID.

        :returns: an :class:`~deezer.resources.Artist` object
        """
        return self.request("GET", f"artist/{artist_id}")

    def get_chart(self) -> Chart:
        """
        Get overall charts for tracks, albums, artists and playlists.

        Combines charts of several resources in one endpoint.

        :returns: a :class:`~deezer.resources.Chart` instance.
        """
        return self.request("GET", "chart", resource_type=Chart)

    def get_tracks_chart(self) -> List[Track]:
        """
        Get top tracks.

        :return: a list of :class:`~deezer.resources.Track` instances.
        """
        return self.request("GET", "chart/0/tracks")

    def get_albums_chart(self) -> List[Album]:
        """
        Get top albums.

        :return: a list of :class:`~deezer.resources.Album` instances.
        """
        return self.request("GET", "chart/0/albums")

    def get_artists_chart(self) -> List[Artist]:
        """
        Get top artists.

        :return: a list of :class:`~deezer.resources.Artist` instances.
        """
        return self.request("GET", "chart/0/artists")

    def get_playlists_chart(self) -> List[Playlist]:
        """
        Get top playlists.

        :return: a list of :class:`~deezer.resources.Playlist` instances.
        """
        return self.request("GET", "chart/0/playlists")

    def get_podcasts_chart(self) -> List[Podcast]:
        """
        Get top podcasts.

        :return: a list of :class:`~deezer.resources.Podcasts` instances.
        """
        return self.request("GET", "chart/0/podcasts")

    def get_episode(self, episode_id: int) -> Episode:
        """
        Get the episode with the given ID.

        :returns: a :class:`~deezer.resources.Episode` object
        """
        return self.request("GET", f"episode/{episode_id}")

    def get_genre(self, genre_id: int) -> Genre:
        """
        Get the genre with the given ID

        :returns: a :class:`~deezer.resources.Genre` object
        """
        return self.request("GET", f"genre/{genre_id}")

    def list_genres(self) -> List[Genre]:
        """
        List musical genres.

        :returns: a list of :class:`~deezer.resources.Genre` objects.
        """
        return self.request("GET", "genre")

    def get_playlist(self, playlist_id: int) -> Playlist:
        """
        Get the playlist with the given ID.

        :returns: a :class:`~deezer.resources.Playlist` object
        """
        return self.request("GET", f"playlist/{playlist_id}")

    def get_podcast(self, podcast_id: int) -> Podcast:
        """
        Get the podcast with the given ID.

        :returns: a :class:`~deezer.resources.Podcast` object
        """
        return self.request("GET", f"podcast/{podcast_id}")

    def get_radio(self, radio_id: int) -> Radio:
        """
        Get the radio with the given ID..

        :returns: a :class:`~deezer.resources.Radio` object
        """
        return self.request("GET", f"radio/{radio_id}")

    def list_radios(self) -> List[Radio]:
        """
        List radios.

        :returns: a list of :class:`~deezer.resources.Radio` objects
        """
        return self.request("GET", "radio")

    def get_radios_top(self):
        """
        Get the top radios (5 radios).

        :returns: a :class:`~deezer.resources.Radio` object
        """
        return self.request("GET", "radio/top")

    def get_track(self, track_id: int) -> Track:
        """
        Get the track with the given ID.

        :returns: a :class:`~deezer.resources.Track` object
        """
        return self.request("GET", f"track/{track_id}")

    def get_user(self, user_id: Optional[int] = None) -> User:
        """
        Get the user with the given ID.

        :returns: a :class:`~deezer.resources.User` object
        """
        user_id_str = str(user_id) if user_id else "me"
        return self.request("GET", f"user/{user_id_str}")

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

    def _search(
        self,
        path: str,
        query: str = "",
        strict: Optional[bool] = None,
        ordering: Optional[str] = None,
        index: Optional[int] = None,
        limit: Optional[int] = None,
        **advanced_params: Optional[Union[str, int]],
    ):
        optional_params = {}
        if strict is True:
            optional_params["strict"] = "on"
        if ordering:
            optional_params["ordering"] = ordering
        if index:
            optional_params["index"] = index
        if limit:
            optional_params["limit"] = limit
        query_parts = []
        if query:
            query_parts.append(query)
        for param_name, param_value in advanced_params.items():
            if param_value:
                query_parts.append(f'{param_name}:"{param_value}"')
        return self.request(
            "GET",
            f"search/{path}" if path else "search",
            q=" ".join(query_parts),
            **optional_params,
        )

    def search(
        self,
        query: str = "",
        strict: Optional[bool] = None,
        ordering: Optional[str] = None,
        artist: Optional[str] = None,
        album: Optional[str] = None,
        track: Optional[str] = None,
        label: Optional[str] = None,
        dur_min: Optional[int] = None,
        dur_max: Optional[int] = None,
        bpm_min: Optional[int] = None,
        bpm_max: Optional[int] = None,
        index: Optional[int] = None,
        limit: Optional[int] = None,
    ):
        """
        Search tracks.

        Advanced search is available by either formatting the query yourself or
        by using the dedicated keywords arguments.

        :param query: the query to search for, this is directly passed as q query.
        :param strict: whether to disable fuzzy search and enable strict mode.
        :param ordering: see Deezer's API docs for possible values.
        :param artist: parameter for the advanced search feature.
        :param album: parameter for the advanced search feature.
        :param track: parameter for the advanced search feature.
        :param label: parameter for the advanced search feature.
        :param dur_min: parameter for the advanced search feature.
        :param dur_max: parameter for the advanced search feature.
        :param bpm_min: parameter for the advanced search feature.
        :param bpm_max: parameter for the advanced search feature.
        :param index: the offset of the first object you want to get.
        :param limit: the maximum number of objects to return.
        :returns: a list of :class:`~deezer.resources.Track` instances.
        """
        return self._search(
            "",
            query=query,
            strict=strict,
            ordering=ordering,
            artist=artist,
            album=album,
            track=track,
            label=label,
            dur_min=dur_min,
            dur_max=dur_max,
            bpm_min=bpm_min,
            bpm_max=bpm_max,
            index=index,
            limit=limit,
        )

    def search_albums(
        self,
        query: str = "",
        strict: Optional[bool] = None,
        ordering: Optional[str] = None,
        index: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> List[Album]:
        """
        Search albums matching the given query.

        :param query: the query to search for, this is directly passed as q query.
        :param strict: whether to disable fuzzy search and enable strict mode.
        :param ordering: see Deezer's API docs for possible values.
        :param index: the offset of the first object you want to get.
        :param limit: the maximum number of objects to return.
        :return: list of :class:`~deezer.resources.Album` instances.
        """
        return self._search(
            path="album",
            query=query,
            strict=strict,
            ordering=ordering,
            index=index,
            limit=limit,
        )

    def search_artists(
        self,
        query: str = "",
        strict: Optional[bool] = None,
        ordering: Optional[str] = None,
        index: Optional[int] = None,
        limit: Optional[int] = None,
    ) -> List[Artist]:
        """
        Search artists matching the given query.

        :param query: the query to search for, this is directly passed as q query.
        :param strict: whether to disable fuzzy search and enable strict mode.
        :param ordering: see Deezer's API docs for possible values.
        :param index: the offset of the first object you want to get.
        :param limit: the maximum number of objects to return.
        :return: list of :class:`~deezer.resources.Album` instances.
        """
        return self._search(
            path="artist",
            query=query,
            strict=strict,
            ordering=ordering,
            index=index,
            limit=limit,
        )
