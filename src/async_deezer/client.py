from __future__ import annotations

from typing import Any, ClassVar

import httpx
from httpx._types import HeaderTypes

from deezer.auth import DeezerQueryAuth
from deezer.exceptions import (
    DeezerErrorResponse,
    DeezerHTTPError,
    DeezerUnknownResource,
)
from .pagination import AsyncPaginatedList
from .resources import (
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


class AsyncClient(httpx.AsyncClient):
    """
    Asynchronous Deezer API client.

    This mirrors the public API of :class:`deezer.Client`, but uses an
    :class:`httpx.AsyncClient` under the hood so that all network operations
    are non-blocking.
    """

    objects_types: ClassVar[dict[str, type[Resource] | None]] = {
        "album": Album,
        "artist": Artist,
        "chart": Chart,
        "editorial": Editorial,
        "episode": Episode,
        "genre": Genre,
        "playlist": Playlist,
        "podcast": Podcast,
        "radio": Radio,
        "track": Track,
        "user": User,
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

    def _process_json(
        self,
        item: dict[str, Any],
        parent: Resource | None = None,
        resource_type: type[Resource] | None = None,
        resource_id: int | None = None,
        paginate_list: bool = False,
    ):
        """
        Recursively convert dictionary to :class:`~deezer.Resource` object.

        This is intentionally kept synchronous, as it only manipulates in-memory
        Python objects.
        """
        if "data" in item:
            parsed_data = [self._process_json(i, parent, paginate_list=False) for i in item["data"]]
            if not paginate_list:
                return parsed_data
            item["data"] = parsed_data
            return item

        result: dict[str, Any] = {}
        for key, value in item.items():
            if isinstance(value, dict) and ("type" in value or "data" in value):
                value = self._process_json(value, parent)
            result[key] = value
        if parent is not None:
            result[parent.type] = parent

        if "id" not in result and resource_id is not None:
            result["id"] = resource_id

        if "type" in result and result["type"] in self.objects_types:
            object_class = self.objects_types[result["type"]]
        elif "type" in result or (not resource_type and "id" in result):
            # in case any new types are introduced by the API
            object_class = Resource
        elif resource_type:
            object_class = resource_type
        elif item.get("results") is True:
            return True
        else:
            raise DeezerUnknownResource(f"Unable to find resource type for {result!r}")
        assert object_class is not None  # noqa: S101
        return object_class(self, result)

    async def request(  # type: ignore[override]
        self,
        method: str,
        path: str,
        parent: Resource | None = None,
        resource_type: type[Resource] | None = None,
        resource_id: int | None = None,
        paginate_list: bool = False,
        **kwargs: Any,
    ):
        """
        Make an asynchronous request to the API and parse the response.
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

    # High level methods – mirror deezer.Client but return awaitables.

    def _get_paginated_list(self, path: str, params: dict | None = None) -> AsyncPaginatedList:
        """
        Build an :class:`AsyncPaginatedList` bound to this client.

        Constructing the object itself is synchronous and does not perform
        any network I/O; actual page fetching happens when you iterate over
        it with ``async for`` or use its async helpers.
        """
        return AsyncPaginatedList(client=self, base_path=path, params=params)

    async def get_album(self, album_id: int) -> Album:
        return await self.request("GET", f"album/{album_id}")

    async def get_artist(self, artist_id: int) -> Artist:
        return await self.request("GET", f"artist/{artist_id}")

    async def get_chart(self, genre_id: int = 0) -> Chart:
        return await self.request(
            "GET",
            f"chart/{genre_id}",
            resource_type=Chart,
            resource_id=genre_id,
        )

    async def get_tracks_chart(self, genre_id: int = 0) -> list[Track]:
        return await self.request("GET", f"chart/{genre_id}/tracks")

    async def get_albums_chart(self, genre_id: int = 0) -> list[Album]:
        return await self.request("GET", f"chart/{genre_id}/albums")

    async def get_artists_chart(self, genre_id: int = 0) -> list[Artist]:
        return await self.request("GET", f"chart/{genre_id}/artists")

    async def get_playlists_chart(self, genre_id: int = 0) -> list[Playlist]:
        return await self.request("GET", f"chart/{genre_id}/playlists")

    async def get_podcasts_chart(self, genre_id: int = 0) -> list[Podcast]:
        return await self.request("GET", f"chart/{genre_id}/podcasts")

    async def get_editorial(self, editorial_id: int) -> Editorial:
        return await self.request("GET", f"editorial/{editorial_id}")

    def list_editorials(self) -> AsyncPaginatedList[Editorial]:
        return self._get_paginated_list("editorial")

    async def get_episode(self, episode_id: int) -> Episode:
        return await self.request("GET", f"episode/{episode_id}")

    async def get_genre(self, genre_id: int) -> Genre:
        return await self.request("GET", f"genre/{genre_id}")

    async def list_genres(self) -> list[Genre]:
        return await self.request("GET", "genre")

    async def get_playlist(self, playlist_id: int) -> Playlist:
        return await self.request("GET", f"playlist/{playlist_id}")

    async def get_podcast(self, podcast_id: int) -> Podcast:
        return await self.request("GET", f"podcast/{podcast_id}")

    async def get_radio(self, radio_id: int) -> Radio:
        return await self.request("GET", f"radio/{radio_id}")

    async def list_radios(self) -> list[Radio]:
        return await self.request("GET", "radio")

    def get_radios_top(self) -> AsyncPaginatedList[Radio]:
        return self._get_paginated_list("radio/top")

    async def get_track(self, track_id: int) -> Track:
        return await self.request("GET", f"track/{track_id}")

    async def get_user(self, user_id: int | None = None) -> User:
        user_id_str = str(user_id) if user_id else "me"
        return await self.request("GET", f"user/{user_id_str}")

    def get_user_recommended_tracks(self, **kwargs) -> AsyncPaginatedList[Track]:
        return AsyncPaginatedList(
            client=self,
            base_path="user/me/recommendations/tracks",
            params=kwargs or None,
        )

    def get_user_recommended_albums(self, **kwargs) -> AsyncPaginatedList[Album]:
        return AsyncPaginatedList(
            client=self,
            base_path="user/me/recommendations/albums",
            params=kwargs or None,
        )

    def get_user_recommended_artists(self, **kwargs) -> AsyncPaginatedList[Artist]:
        return AsyncPaginatedList(
            client=self,
            base_path="user/me/recommendations/artists",
            params=kwargs or None,
        )

    def get_user_recommended_playlists(self, **kwargs) -> AsyncPaginatedList[Playlist]:
        return AsyncPaginatedList(
            client=self,
            base_path="user/me/recommendations/playlists",
            params=kwargs or None,
        )

    def get_user_flow(self, **kwargs) -> AsyncPaginatedList[Track]:
        return AsyncPaginatedList(
            client=self,
            base_path="user/me/flow",
            params=kwargs or None,
        )

    def get_user_albums(self, user_id: int | None = None) -> AsyncPaginatedList[Album]:
        user_id_str = str(user_id) if user_id else "me"
        return self._get_paginated_list(f"user/{user_id_str}/albums")

    async def add_user_album(self, album_id: int) -> bool:
        return await self.request(
            "POST",
            "user/me/albums",
            params={"album_id": album_id},
        )

    async def remove_user_album(self, album_id: int) -> bool:
        return await self.request(
            "DELETE",
            "user/me/albums",
            params={"album_id": album_id},
        )

    def get_user_artists(self, user_id: int | None = None) -> AsyncPaginatedList[Artist]:
        user_id_str = str(user_id) if user_id else "me"
        return self._get_paginated_list(f"user/{user_id_str}/artists")

    async def add_user_artist(self, artist_id: int) -> bool:
        return await self.request(
            "POST",
            "user/me/artists",
            params={"artist_id": artist_id},
        )

    async def remove_user_artist(self, artist_id: int) -> bool:
        return await self.request(
            "DELETE",
            "user/me/artists",
            params={"artist_id": artist_id},
        )

    def get_user_followers(self, user_id: int | None = None) -> AsyncPaginatedList[User]:
        user_id_str = str(user_id) if user_id else "me"
        return self._get_paginated_list(f"user/{user_id_str}/followers")

    def get_user_followings(self, user_id: int | None = None) -> AsyncPaginatedList[User]:
        user_id_str = str(user_id) if user_id else "me"
        return self._get_paginated_list(f"user/{user_id_str}/followings")

    async def add_user_following(self, user_id: int) -> bool:
        return await self.request(
            "POST",
            "user/me/followings",
            params={"user_id": user_id},
        )

    async def remove_user_following(self, user_id: int) -> bool:
        return await self.request(
            "DELETE",
            "user/me/followings",
            params={"user_id": user_id},
        )

    def get_user_history(self) -> AsyncPaginatedList[Track]:
        return self._get_paginated_list("user/me/history")

    def get_user_tracks(self, user_id: int | None = None) -> AsyncPaginatedList[Track]:
        user_id_str = str(user_id) if user_id else "me"
        return self._get_paginated_list(f"user/{user_id_str}/tracks")

    async def add_user_track(self, track_id: int) -> bool:
        return await self.request(
            "POST",
            "user/me/tracks",
            params={"track_id": track_id},
        )

    async def remove_user_track(self, track_id: int) -> bool:
        return await self.request(
            "DELETE",
            "user/me/tracks",
            params={"track_id": track_id},
        )

    async def remove_user_playlist(self, playlist_id: int) -> bool:
        return await self.request(
            "DELETE",
            "user/me/playlists",
            params={"playlist_id": playlist_id},
        )

    async def add_user_playlist(self, playlist_id: int) -> bool:
        return await self.request(
            "POST",
            "user/me/playlists",
            params={"playlist_id": playlist_id},
        )

    async def create_playlist(self, playlist_name: str) -> int:
        result = await self.request(
            "POST",
            "user/me/playlists",
            params={"title": playlist_name},
        )
        return result.id

    async def delete_playlist(self, playlist_id: int) -> bool:
        return await self.request("DELETE", f"playlist/{playlist_id}")

    def _search(
        self,
        path: str,
        query: str = "",
        strict: bool | None = None,
        ordering: str | None = None,
        **advanced_params: str | int | None,
    ):
        optional_params: dict[str, str] = {}
        if strict is True:
            optional_params["strict"] = "on"
        if ordering:
            optional_params["ordering"] = ordering
        query_parts: list[str] = []
        if query:
            query_parts.append(query)
        query_parts.extend(
            f'{param_name}:"{param_value}"'
            for param_name, param_value in advanced_params.items()
            if param_value is not None
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
    ) -> AsyncPaginatedList[Track]:
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
    ) -> AsyncPaginatedList[Album]:
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
    ) -> AsyncPaginatedList[Artist]:
        return self._search(
            path="artist",
            query=query,
            strict=strict,
            ordering=ordering,
        )

    def search_playlists(
        self,
        query: str = "",
        strict: bool | None = None,
        ordering: str | None = None,
    ) -> AsyncPaginatedList[Playlist]:
        return self._search(
            path="playlist",
            query=query,
            strict=strict,
            ordering=ordering,
        )