from __future__ import annotations

from typing import Any

import requests

from deezer.exceptions import (
    DeezerErrorResponse,
    DeezerHTTPError,
    DeezerUnknownResource,
)
from deezer.pagination import PaginatedList
from deezer.resources import (
    Album,
    Artist,
    Chart,
    Editorial,
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
    A client to retrieve some basic infos about Deezer resources.

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
        "editorial": Editorial,
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

        headers = headers or {}
        self.session.headers.update(headers)

    def _process_json(
        self,
        item: dict[str, Any],
        parent: Resource | None = None,
        resource_type: type[Resource] | None = None,
        resource_id: int | None = None,
        paginate_list=False,
    ):
        """
        Recursively convert dictionary
        to :class:`~deezer.Resource` object

        :param item: the JSON response as dict.
        :param parent: A reference to the parent resource, to avoid fetching again.
        :param resource_type: The resource class to use as top level.
        :param resource_id: The resource id to use as top level.
        :param paginate_list: Whether to wrap list into a pagination object.
        :returns: instance of :class:`~deezer.Resource`
        """
        if "data" in item:
            parsed_data = [
                self._process_json(i, parent, paginate_list=False) for i in item["data"]
            ]
            if not paginate_list:
                return parsed_data
            item["data"] = parsed_data
            return item

        result = {}
        for key, value in item.items():
            if isinstance(value, dict) and ("type" in value or "data" in value):
                value = self._process_json(value, parent)
            result[key] = value
        if parent is not None:
            result[parent.type] = parent

        if "id" not in result and resource_id is not None:
            result["id"] = resource_id

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
        assert object_class is not None  # nosec B101
        return object_class(self, result)

    def request(
        self,
        method: str,
        path: str,
        parent: Resource | None = None,
        resource_type: type[Resource] | None = None,
        resource_id: int | None = None,
        paginate_list=False,
        **params,
    ):
        """
        Make a request to the API and parse the response.

        :param method: HTTP verb to use: GET, POST< DELETE, ...
        :param path: The path to make the API call to (e.g. 'artist/1234').
        :param parent: A reference to the parent resource, to avoid fetching again.
        :param resource_type: The resource class to use as top level.
        :param resource_id: The resource id to use as top level.
        :param paginate_list: Whether to wrap list into a pagination object.
        :param params: Query parameters to add to the request
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
        return self._process_json(
            json_data,
            parent=parent,
            resource_type=resource_type,
            resource_id=resource_id,
            paginate_list=paginate_list,
        )

    def _get_paginated_list(self, path, **params):
        return PaginatedList(client=self, base_path=path, **params)

    def get_album(self, album_id: int) -> Album:
        """
        Get the album with the given ID.

        :returns: an :class:`~deezer.Album` object
        """
        return self.request("GET", f"album/{album_id}")

    def get_artist(self, artist_id: int) -> Artist:
        """
        Get the artist with the given ID.

        :returns: an :class:`~deezer.Artist` object
        """
        return self.request("GET", f"artist/{artist_id}")

    def get_chart(self, genre_id: int = 0) -> Chart:
        """
        Get overall charts for tracks, albums, artists and playlists for the given genre ID.

        Combine charts of several resources in one endpoint.

        :param genre_id: the genre ID, default to `All` genre (genre_id = 0).
        :returns: a :class:`~deezer.Chart` instance.
        """
        return self.request(
            "GET", f"chart/{genre_id}", resource_type=Chart, resource_id=genre_id
        )

    def get_tracks_chart(self, genre_id: int = 0) -> list[Track]:
        """
        Get top tracks for the given genre ID.

        :param genre_id: the genre ID, default to `All` genre (genre_id = 0).
        :return: a list of :class:`~deezer.Track` instances.
        """
        return self.request("GET", f"chart/{genre_id}/tracks")

    def get_albums_chart(self, genre_id: int = 0) -> list[Album]:
        """
        Get top albums for the given genre ID.

        :param genre_id: the genre ID, default to `All` genre (genre_id = 0).
        :return: a list of :class:`~deezer.Album` instances.
        """
        return self.request("GET", f"chart/{genre_id}/albums")

    def get_artists_chart(self, genre_id: int = 0) -> list[Artist]:
        """
        Get top artists for the given genre ID.

        :param genre_id: the genre ID, default to `All` genre (genre_id = 0).
        :return: a list of :class:`~deezer.Artist` instances.
        """
        return self.request("GET", f"chart/{genre_id}/artists")

    def get_playlists_chart(self, genre_id: int = 0) -> list[Playlist]:
        """
        Get top playlists for the given genre ID.

        :param genre_id: the genre ID, default to `All` genre (genre_id = 0).
        :return: a list of :class:`~deezer.Playlist` instances.
        """
        return self.request("GET", f"chart/{genre_id}/playlists")

    def get_podcasts_chart(self, genre_id: int = 0) -> list[Podcast]:
        """
        Get top podcasts for the given genre ID.

        :param genre_id: the genre ID, default to `All` genre (genre_id = 0).
        :return: a list of :class:`~deezer.Podcast` instances.
        """
        return self.request("GET", f"chart/{genre_id}/podcasts")

    def get_editorial(self, editorial_id: int) -> Editorial:
        """
        Get the editorial with the given ID.

        :returns: a :class:`~deezer.Editorial` object.
        """
        return self.request("GET", f"editorial/{editorial_id}")

    def list_editorials(self) -> PaginatedList[Editorial]:
        """
        List editorials.

        :returns: a :class:`~deezer.pagination.PaginatedList`
                  of :class:`~deezer.Editorial` objects.
        """
        return self._get_paginated_list("editorial")

    def get_episode(self, episode_id: int) -> Episode:
        """
        Get the episode with the given ID.

        :returns: a :class:`~deezer.Episode` object
        """
        return self.request("GET", f"episode/{episode_id}")

    def get_genre(self, genre_id: int) -> Genre:
        """
        Get the genre with the given ID

        :returns: a :class:`~deezer.Genre` object
        """
        return self.request("GET", f"genre/{genre_id}")

    def list_genres(self) -> list[Genre]:
        """
        List musical genres.

        :return: a list of :class:`~deezer.Genre` instances
        """
        return self.request("GET", "genre")

    def get_playlist(self, playlist_id: int) -> Playlist:
        """
        Get the playlist with the given ID.

        :returns: a :class:`~deezer.Playlist` object
        """
        return self.request("GET", f"playlist/{playlist_id}")

    def get_podcast(self, podcast_id: int) -> Podcast:
        """
        Get the podcast with the given ID.

        :returns: a :class:`~deezer.Podcast` object
        """
        return self.request("GET", f"podcast/{podcast_id}")

    def get_radio(self, radio_id: int) -> Radio:
        """
        Get the radio with the given ID.

        :returns: a :class:`~deezer.Radio` object
        """
        return self.request("GET", f"radio/{radio_id}")

    def list_radios(self) -> list[Radio]:
        """
        List radios.

        :return: a list of :class:`~deezer.Radio` instances
        """
        return self.request("GET", "radio")

    def get_radios_top(self) -> PaginatedList[Radio]:
        """
        Get the top radios.

        :returns: a :class:`~deezer.pagination.PaginatedList`
                  of :class:`~deezer.Radio` objects.
        """
        return self._get_paginated_list("radio/top")

    def get_track(self, track_id: int) -> Track:
        """
        Get the track with the given ID.

        :returns: a :class:`~deezer.Track` object
        """
        return self.request("GET", f"track/{track_id}")

    def get_user(self, user_id: int | None = None) -> User:
        """
        Get the user with the given ID.

        :returns: a :class:`~deezer.User` object
        """
        user_id_str = str(user_id) if user_id else "me"
        return self.request("GET", f"user/{user_id_str}")

    def get_user_albums(self, user_id: int | None = None) -> PaginatedList[Album]:
        """
        Get the favourites albums for the given user_id if provided or current user if not.

        :param user_id: the user ID to get favourites albums.
        :returns: a :class:`~deezer.pagination.PaginatedList`
                  of :class:`~deezer.Album` objects.
        """
        user_id_str = str(user_id) if user_id else "me"
        return self._get_paginated_list(f"user/{user_id_str}/albums")

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

    def get_user_artists(self, user_id: int | None = None) -> PaginatedList[Artist]:
        """
        Get the favourites artists for the given user_id if provided or current user if not.

        :param user_id: the user ID to get favourites artists.
        :return: a :class:`~deezer.pagination.PaginatedList`
                 of :class:`~deezer.Artist` instances.
        """
        user_id_str = str(user_id) if user_id else "me"
        return self._get_paginated_list(f"user/{user_id_str}/artists")

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

    def get_user_followers(self, user_id: int | None = None) -> PaginatedList[User]:
        """
        Get the followers for the given user_id if provided or current user if not.

        :param user_id: the user ID to get followers.
        :returns: a :class:`~deezer.pagination.PaginatedList`
                 of :class:`~deezer.User` instances.
        """
        user_id_str = str(user_id) if user_id else "me"
        return self._get_paginated_list(f"user/{user_id_str}/followers")

    def get_user_followings(self, user_id: int | None = None) -> PaginatedList[User]:
        """
        Get the followings for the given user_id if provided or current user if not.

        :param user_id: the user ID to get followings.
        :returns: a :class:`~deezer.pagination.PaginatedList`
                 of :class:`~deezer.User` instances.
        """
        user_id_str = str(user_id) if user_id else "me"
        return self._get_paginated_list(f"user/{user_id_str}/followings")

    def add_user_following(self, user_id: int) -> bool:
        """
        Follow the given user ID as the currently authenticated user.

        :param user_id: the ID of the user to follow.
        :return: boolean whether the operation succeeded.
        """
        return self.request("POST", "user/me/followings", user_id=user_id)

    def remove_user_following(self, user_id: int) -> bool:
        """
        Stop following the given user ID as the currently authenticated user.

        :param user_id: the ID of the user to stop following.
        :return: boolean whether the operation succeeded.
        """
        return self.request("DELETE", "user/me/followings", user_id=user_id)

    def get_user_history(self) -> PaginatedList[Track]:
        """
        Returns a list of the recently played tracks for the current user.

        :return: a :class:`~deezer.pagination.PaginatedList`
                 of :class:`~deezer.Track` instances.
        """
        return self._get_paginated_list("user/me/history")

    def get_user_tracks(self, user_id: int | None = None) -> PaginatedList[Track]:
        """
        Get the favourites tracks for the given user_id if provided or current user if not.

        :param user_id: the user ID to get favourites tracks.
        :return: a :class:`~deezer.pagination.PaginatedList`
                 of :class:`~deezer.Track` instances.
        """
        user_id_str = str(user_id) if user_id else "me"
        return self._get_paginated_list(f"user/{user_id_str}/tracks")

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
        strict: bool | None = None,
        ordering: str | None = None,
        **advanced_params: str | int | None,
    ):
        optional_params = {}
        if strict is True:
            optional_params["strict"] = "on"
        if ordering:
            optional_params["ordering"] = ordering
        query_parts = []
        if query:
            query_parts.append(query)
        query_parts.extend(
            f'{param_name}:"{param_value}"'
            for param_name, param_value in advanced_params.items()
            if param_value
        )

        return self._get_paginated_list(
            path=f"search/{path}" if path else "search",
            q=" ".join(query_parts),
            **optional_params,
        )

    def search(
        self,
        query: str = "",
        strict: bool | None = None,
        ordering: str | None = None,
        artist: str | None = None,
        album: str | None = None,
        track: str | None = None,
        label: str | None = None,
        dur_min: int | None = None,
        dur_max: int | None = None,
        bpm_min: int | None = None,
        bpm_max: int | None = None,
    ):
        """
        Search tracks.

        Advanced search is available by either formatting the query yourself or
        by using the dedicated keywords arguments.

        :param query: the query to search for, this is directly passed as q query.
        :param strict: whether to disable fuzzy search and enable strict mode.
        :param ordering: see Deezer API docs for possible values.
        :param artist: parameter for the advanced search feature.
        :param album: parameter for the advanced search feature.
        :param track: parameter for the advanced search feature.
        :param label: parameter for the advanced search feature.
        :param dur_min: parameter for the advanced search feature.
        :param dur_max: parameter for the advanced search feature.
        :param bpm_min: parameter for the advanced search feature.
        :param bpm_max: parameter for the advanced search feature.
        :returns: a list of :class:`~deezer.Track` instances.
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
        )

    def search_albums(
        self,
        query: str = "",
        strict: bool | None = None,
        ordering: str | None = None,
    ) -> PaginatedList[Album]:
        """
        Search albums matching the given query.

        :param query: the query to search for, this is directly passed as q query.
        :param strict: whether to disable fuzzy search and enable strict mode.
        :param ordering: see Deezer API docs for possible values.
        :return: list of :class:`~deezer.Album` instances.
        """
        return self._search(
            path="album",
            query=query,
            strict=strict,
            ordering=ordering,
        )

    def search_artists(
        self,
        query: str = "",
        strict: bool | None = None,
        ordering: str | None = None,
    ) -> PaginatedList[Artist]:
        """
        Search artists matching the given query.

        :param query: the query to search for, this is directly passed as q query.
        :param strict: whether to disable fuzzy search and enable strict mode.
        :param ordering: see Deezer API docs for possible values.
        :return: list of :class:`~deezer.Album` instances.
        """
        return self._search(
            path="artist",
            query=query,
            strict=strict,
            ordering=ordering,
        )
