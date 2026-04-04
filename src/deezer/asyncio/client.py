from __future__ import annotations

from typing import ClassVar

import httpx
from httpx._types import HeaderTypes

from deezer._mixin import DeezerMixin
from deezer.auth import DeezerQueryAuth
from deezer.exceptions import (
    DeezerErrorResponse,
    DeezerHTTPError,
)
from deezer.resources import Resource

from .pagination import AsyncPaginatedList
from .resources import (
    AsyncAlbum,
    AsyncArtist,
    AsyncChart,
    AsyncEditorial,
    AsyncEpisode,
    AsyncGenre,
    AsyncPlaylist,
    AsyncPodcast,
    AsyncRadio,
    AsyncResource,
    AsyncTrack,
    AsyncUser,
)


class AsyncClient(DeezerMixin, httpx.AsyncClient):
    """
    An async client to retrieve some basic infos about Deezer resources.

    Create a client instance with the given options. Options should
    be passed in to the constructor as kwargs.

        >>> from deezer.asyncio import AsyncClient
        >>> client = AsyncClient()

    This client provides several async methods to retrieve the content of
    Deezer objects, based on their json structure.

    Headers can be forced by using the ``headers`` kwarg.
    For example, use ``Accept-Language`` header to force the output language.

        >>> from deezer.asyncio import AsyncClient
        >>> client = AsyncClient(headers={'Accept-Language': 'fr'})

    :param access_token: user access token.
    :param headers: a dictionary of headers to be used.
    """

    _resource_base_class: ClassVar[type[AsyncResource]] = AsyncResource

    objects_types: ClassVar[dict[str, type[AsyncResource] | None]] = {
        "album": AsyncAlbum,
        "artist": AsyncArtist,
        "chart": AsyncChart,
        "editorial": AsyncEditorial,
        "episode": AsyncEpisode,
        "genre": AsyncGenre,
        "playlist": AsyncPlaylist,
        "podcast": AsyncPodcast,
        "radio": AsyncRadio,
        "track": AsyncTrack,
        "user": AsyncUser,
    }

    def __init__(
        self,
        access_token: str | None = None,
        headers: HeaderTypes | None = None,
    ):
        if access_token:
            deezer_auth = DeezerQueryAuth(access_token=access_token)
        else:
            deezer_auth = None
        super().__init__(
            base_url="https://api.deezer.com",
            auth=deezer_auth,
            headers=headers,
        )

    async def request(  # ty: ignore[invalid-method-override]
        self,
        method: str,
        path: str,
        parent: AsyncResource | Resource | None = None,
        resource_type: type[AsyncResource] | type[Resource] | None = None,
        resource_id: int | None = None,
        paginate_list=False,
        **kwargs,
    ):
        """
        Make a request to the API and parse the response.

        :param method: HTTP verb to use: GET, POST, DELETE, ...
        :param path: The path to make the API call to (e.g. 'artist/1234').
        :param parent: A reference to the parent resource, to avoid fetching again.
        :param resource_type: The resource class to use as top level.
        :param resource_id: The resource id to use as top level.
        :param paginate_list: Whether to wrap list into a pagination object.
        """
        response = await super().request(
            method,
            path,
            **kwargs,
        )
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as exc:
            raise DeezerHTTPError.from_http_error(exc) from exc
        json_data = response.json()
        if not isinstance(json_data, dict):
            return json_data
        if json_data.get("error"):
            raise DeezerErrorResponse(json_data)
        return self._process_json(
            json_data,
            parent=parent,
            resource_type=resource_type,
            resource_id=resource_id,
            paginate_list=paginate_list,
        )

    def _get_paginated_list(self, path: str, params: dict | None = None):
        return AsyncPaginatedList(client=self, base_path=path, params=params)

    async def get_artist(self, artist_id: int) -> AsyncArtist:
        """
        Get the artist with the given ID.

        :returns: an :class:`~deezer.asyncio.AsyncArtist` object
        """
        return await self.request("GET", f"artist/{artist_id}")

    async def get_album(self, album_id: int) -> AsyncAlbum:
        """
        Get the album with the given ID.

        :returns: an :class:`~deezer.asyncio.AsyncAlbum` object
        """
        return await self.request("GET", f"album/{album_id}")

    async def get_track(self, track_id: int) -> AsyncTrack:
        """
        Get the track with the given ID.

        :returns: an :class:`~deezer.asyncio.AsyncTrack` object
        """
        return await self.request("GET", f"track/{track_id}")

    async def get_genre(self, genre_id: int) -> AsyncGenre:
        """
        Get the genre with the given ID.

        :returns: an :class:`~deezer.asyncio.AsyncGenre` object
        """
        return await self.request("GET", f"genre/{genre_id}")

    async def get_radio(self, radio_id: int) -> AsyncRadio:
        """
        Get the radio with the given ID.

        :returns: an :class:`~deezer.asyncio.AsyncRadio` object
        """
        return await self.request("GET", f"radio/{radio_id}")

    async def get_podcast(self, podcast_id: int) -> AsyncPodcast:
        """
        Get the podcast with the given ID.

        :returns: an :class:`~deezer.asyncio.AsyncPodcast` object
        """
        return await self.request("GET", f"podcast/{podcast_id}")

    async def get_episode(self, episode_id: int) -> AsyncEpisode:
        """
        Get the episode with the given ID.

        :returns: an :class:`~deezer.asyncio.AsyncEpisode` object
        """
        return await self.request("GET", f"episode/{episode_id}")

    async def get_editorial(self, editorial_id: int) -> AsyncEditorial:
        """
        Get the editorial with the given ID.

        :returns: an :class:`~deezer.asyncio.AsyncEditorial` object
        """
        return await self.request("GET", f"editorial/{editorial_id}")

    async def get_playlist(self, playlist_id: int) -> AsyncPlaylist:
        """
        Get the playlist with the given ID.

        :returns: an :class:`~deezer.asyncio.AsyncPlaylist` object
        """
        return await self.request("GET", f"playlist/{playlist_id}")

    async def get_user(self, user_id: int | None = None) -> AsyncUser:
        """
        Get the user with the given ID.

        :returns: an :class:`~deezer.asyncio.AsyncUser` object
        """
        user_id_str = str(user_id) if user_id else "me"
        return await self.request("GET", f"user/{user_id_str}")

    async def get_chart(self, genre_id: int = 0) -> AsyncChart:
        """
        Get overall charts for the given genre ID.

        :returns: an :class:`~deezer.asyncio.AsyncChart` object
        """
        return await self.request("GET", f"chart/{genre_id}", resource_type=AsyncChart, resource_id=genre_id)

    def list_editorials(self) -> AsyncPaginatedList:
        """
        List editorials.

        :returns: an :class:`AsyncPaginatedList` of :class:`AsyncEditorial` objects.
        """
        return self._get_paginated_list("editorial")

    async def list_genres(self) -> list[AsyncGenre]:
        """
        List musical genres.

        :returns: a list of :class:`AsyncGenre` instances
        """
        return await self.request("GET", "genre")

    async def list_radios(self) -> list[AsyncRadio]:
        """
        List radios.

        :returns: a list of :class:`AsyncRadio` instances
        """
        return await self.request("GET", "radio")

    def get_radios_top(self) -> AsyncPaginatedList:
        """
        Get the top radios.

        :returns: an :class:`AsyncPaginatedList` of :class:`AsyncRadio` objects.
        """
        return self._get_paginated_list("radio/top")

    def get_user_recommended_tracks(self, **kwargs) -> AsyncPaginatedList:
        """Get user's recommended tracks."""
        return AsyncPaginatedList(client=self, base_path="user/me/recommendations/tracks", **kwargs)

    def get_user_recommended_albums(self, **kwargs) -> AsyncPaginatedList:
        """Get user's recommended albums."""
        return AsyncPaginatedList(client=self, base_path="user/me/recommendations/albums", **kwargs)

    def get_user_recommended_artists(self, **kwargs) -> AsyncPaginatedList:
        """Get user's recommended artists."""
        return AsyncPaginatedList(client=self, base_path="user/me/recommendations/artists", **kwargs)

    def get_user_recommended_playlists(self, **kwargs) -> AsyncPaginatedList:
        """Get user's recommended playlists."""
        return AsyncPaginatedList(client=self, base_path="user/me/recommendations/playlists", **kwargs)

    def get_user_flow(self, **kwargs) -> AsyncPaginatedList:
        """Get user's flow."""
        return AsyncPaginatedList(client=self, base_path="user/me/flow", **kwargs)

    def get_user_albums(self, user_id: int | None = None) -> AsyncPaginatedList:
        """Get the favourites albums for the given user_id or current user."""
        user_id_str = str(user_id) if user_id else "me"
        return self._get_paginated_list(f"user/{user_id_str}/albums")

    async def add_user_album(self, album_id: int) -> bool:
        """Add an album to the user's library."""
        return await self.request("POST", "user/me/albums", params={"album_id": album_id})

    async def remove_user_album(self, album_id: int) -> bool:
        """Remove an album from the user's library."""
        return await self.request("DELETE", "user/me/albums", params={"album_id": album_id})

    def get_user_artists(self, user_id: int | None = None) -> AsyncPaginatedList:
        """Get the favourites artists for the given user_id or current user."""
        user_id_str = str(user_id) if user_id else "me"
        return self._get_paginated_list(f"user/{user_id_str}/artists")

    async def add_user_artist(self, artist_id: int) -> bool:
        """Add an artist to the user's library."""
        return await self.request("POST", "user/me/artists", params={"artist_id": artist_id})

    async def remove_user_artist(self, artist_id: int) -> bool:
        """Remove an artist from the user's library."""
        return await self.request("DELETE", "user/me/artists", params={"artist_id": artist_id})

    def get_user_followers(self, user_id: int | None = None) -> AsyncPaginatedList:
        """Get the followers for the given user_id or current user."""
        user_id_str = str(user_id) if user_id else "me"
        return self._get_paginated_list(f"user/{user_id_str}/followers")

    def get_user_followings(self, user_id: int | None = None) -> AsyncPaginatedList:
        """Get the followings for the given user_id or current user."""
        user_id_str = str(user_id) if user_id else "me"
        return self._get_paginated_list(f"user/{user_id_str}/followings")

    async def add_user_following(self, user_id: int) -> bool:
        """Follow the given user ID as the currently authenticated user."""
        return await self.request("POST", "user/me/followings", params={"user_id": user_id})

    async def remove_user_following(self, user_id: int) -> bool:
        """Stop following the given user ID as the currently authenticated user."""
        return await self.request("DELETE", "user/me/followings", params={"user_id": user_id})

    def get_user_history(self) -> AsyncPaginatedList:
        """Get the recently played tracks for the current user."""
        return self._get_paginated_list("user/me/history")

    def get_user_tracks(self, user_id: int | None = None) -> AsyncPaginatedList:
        """Get the favourites tracks for the given user_id or current user."""
        user_id_str = str(user_id) if user_id else "me"
        return self._get_paginated_list(f"user/{user_id_str}/tracks")

    async def add_user_track(self, track_id: int) -> bool:
        """Add a track to the user's library."""
        return await self.request("POST", "user/me/tracks", params={"track_id": track_id})

    async def remove_user_track(self, track_id: int) -> bool:
        """Remove a track from the user's library."""
        return await self.request("DELETE", "user/me/tracks", params={"track_id": track_id})

    async def add_user_playlist(self, playlist_id: int) -> bool:
        """Add a playlist to the user's library."""
        return await self.request("POST", "user/me/playlists", params={"playlist_id": playlist_id})

    async def remove_user_playlist(self, playlist_id: int) -> bool:
        """Remove a playlist from the user's library."""
        return await self.request("DELETE", "user/me/playlists", params={"playlist_id": playlist_id})

    async def create_playlist(self, playlist_name: str) -> int:
        """
        Create a playlist on the user's account.

        :returns: the ID of the playlist that was created
        """
        result = await self.request("POST", "user/me/playlists", params={"title": playlist_name})
        return result.id

    async def delete_playlist(self, playlist_id: int) -> bool:
        """Delete a playlist from the user's account."""
        return await self.request("DELETE", f"playlist/{playlist_id}")

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
            f'{param_name}:"{param_value}"' for param_name, param_value in advanced_params.items() if param_value
        )

        return self._get_paginated_list(
            path=f"search/{path}" if path else "search",
            params={
                "q": " ".join(query_parts),
                **optional_params,
            },
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
    ) -> AsyncPaginatedList:
        """
        Search tracks.

        Advanced search is available by either formatting the query yourself or
        by using the dedicated keywords arguments.
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
    ) -> AsyncPaginatedList:
        """Search albums matching the given query."""
        return self._search(path="album", query=query, strict=strict, ordering=ordering)

    def search_artists(
        self,
        query: str = "",
        strict: bool | None = None,
        ordering: str | None = None,
    ) -> AsyncPaginatedList:
        """Search artists matching the given query."""
        return self._search(path="artist", query=query, strict=strict, ordering=ordering)

    def search_playlists(
        self,
        query: str = "",
        strict: bool | None = None,
        ordering: str | None = None,
    ) -> AsyncPaginatedList:
        """Search playlists matching the given query."""
        return self._search(path="playlist", query=query, strict=strict, ordering=ordering)
