from __future__ import annotations

import httpx
from httpx._types import HeaderTypes

from deezer._mixin import DeezerMixin
from deezer.auth import DeezerQueryAuth
from deezer.exceptions import (
    DeezerErrorResponse,
    DeezerHTTPError,
)
from deezer.resources import Album, Resource


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

    async def request(  # type: ignore[override]
        self,
        method: str,
        path: str,
        parent: Resource | None = None,
        resource_type: type[Resource] | None = None,
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

    async def get_album(self, album_id: int) -> Album:
        """
        Get the album with the given ID.

        :returns: an :class:`~deezer.Album` object
        """
        return await self.request("GET", f"album/{album_id}")
