from __future__ import annotations

from collections.abc import AsyncGenerator
from typing import TYPE_CHECKING, Generic, TypeVar
from urllib.parse import parse_qs, urlparse

if TYPE_CHECKING:  # pragma: no cover - import used for typing only
    from async_deezer.client import AsyncClient
    from async_deezer.resources import Resource

ResourceType = TypeVar("ResourceType")
REPR_OUTPUT_SIZE = 5


class AsyncPaginatedList(Generic[ResourceType]):
    """
    Asynchronous equivalent of :class:`deezer.pagination.PaginatedList`.

    It exposes an async iterator interface and explicit async helpers instead
    of relying on synchronous ``__iter__`` / ``__getitem__`` that may block.
    """

    def __init__(
        self,
        client: AsyncClient,
        base_path: str,
        parent: Resource | None = None,
        params: dict | None = None,
    ):
        self._elements: list[ResourceType] = []
        self._client = client
        self._base_path = base_path
        self._base_params = params or {}
        self._next_path: str | None = base_path
        self._next_params = params or {}
        self._parent = parent
        self._total: int | None = None

    def __repr__(self) -> str:
        preview = self._elements[: REPR_OUTPUT_SIZE + 1]
        data: list[ResourceType | str] = list(preview)
        if len(data) > REPR_OUTPUT_SIZE:
            data[-1] = "..."
        return f"<{self.__class__.__name__} {data!r}>"

    def __aiter__(self) -> AsyncGenerator[ResourceType, None]:
        async def _iter() -> AsyncGenerator[ResourceType, None]:
            for element in self._elements:
                yield element
            while self._could_grow():
                for element in await self._grow():
                    yield element

        return _iter()

    def _could_grow(self) -> bool:
        return self._next_path is not None

    async def _grow(self) -> list[ResourceType]:
        new_elements = await self._fetch_next_page()
        self._elements.extend(new_elements)
        return new_elements

    async def _fetch_next_page(self) -> list[ResourceType]:
        assert self._next_path is not None  # noqa: S101
        response_payload = await self._client.request(
            "GET",
            self._next_path,
            parent=self._parent,
            paginate_list=True,
            params=self._next_params,
        )
        self._next_path = None
        self._total = response_payload.get("total")
        next_url = response_payload.get("next", None)
        if next_url:
            url_bits = urlparse(next_url)
            self._next_path = url_bits.path.lstrip("/")
            self._next_params = parse_qs(url_bits.query)
        return response_payload["data"]

    async def _fetch_to_index(self, index: int) -> None:
        while len(self._elements) <= index and self._could_grow():
            await self._grow()

    async def aget(self, index: int) -> ResourceType:
        """
        Asynchronously fetch the item at the given index.

        Unlike ``__getitem__`` on the synchronous pagination object, this does
        not block the event loop.
        """
        await self._fetch_to_index(index)
        return self._elements[index]

    async def aslice(self, start: int, stop: int) -> list[ResourceType]:
        """
        Asynchronously fetch a slice of items.

        This ensures that enough elements have been loaded from the API to
        cover the requested range.
        """
        if stop is not None:
            await self._fetch_to_index(stop - 1)
        else:
            while self._could_grow():
                await self._grow()
        return self._elements[start:stop]

    async def get_total(self) -> int:
        """
        Asynchronously get the total number of items across all pages.

        Mirrors the ``total`` property of :class:`deezer.pagination.PaginatedList`.
        """
        if self._total is None:
            params = self._base_params.copy()
            params["limit"] = 1
            response_payload = await self._client.request(
                "GET",
                self._base_path,
                parent=self._parent,
                paginate_list=True,
                params=params,
            )
            self._total = response_payload["total"]
        assert self._total is not None  # noqa: S101
        return self._total
