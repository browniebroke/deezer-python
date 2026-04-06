from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar
from urllib.parse import parse_qs, urlparse

if TYPE_CHECKING:
    from deezer.asyncio.client import AsyncClient
    from deezer.asyncio.resources.resource import AsyncResource

ResourceType = TypeVar("ResourceType")


class AsyncPaginatedList(Generic[ResourceType]):
    """
    Async paginated response from the API, supporting async iteration.

    Instances should be created via the :meth:`create` classmethod,
    which fetches the first page of results eagerly.
    """

    def __init__(
        self,
        client: AsyncClient,
        base_path: str,
        parent: AsyncResource | None = None,
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
        self._iter_index = 0

    @classmethod
    async def create(
        cls,
        client: AsyncClient,
        base_path: str,
        parent: AsyncResource | None = None,
        params: dict | None = None,
    ) -> AsyncPaginatedList[ResourceType]:
        """Create an AsyncPaginatedList and fetch the first page."""
        instance = cls(client=client, base_path=base_path, parent=parent, params=params)
        await instance._grow()
        return instance

    def __repr__(self) -> str:
        """Convenient representation giving a preview of the content."""
        repr_size = 5
        data: list[ResourceType | str] = list(self._elements[: repr_size + 1])
        if len(data) > repr_size:
            data[-1] = "..."
        return f"<{self.__class__.__name__} {data!r}>"

    def __aiter__(self):
        """Return the async iterator."""
        return self._async_iter()

    async def _async_iter(self):
        """Iterate over elements, fetching new pages as needed."""
        yield_index = 0
        while True:
            if yield_index < len(self._elements):
                yield self._elements[yield_index]
                yield_index += 1
            elif self._could_grow():
                await self._grow()
            else:
                break

    async def __anext__(self) -> ResourceType:
        """Get the next item from the list."""
        if self._iter_index < len(self._elements):
            item = self._elements[self._iter_index]
            self._iter_index += 1
            return item
        if self._could_grow():
            new_elements = await self._grow()
            if new_elements and self._iter_index < len(self._elements):
                item = self._elements[self._iter_index]
                self._iter_index += 1
                return item
        raise StopAsyncIteration

    @property
    def total(self) -> int:
        """The total number of items in the list, mirroring what Deezer returns."""
        assert self._total is not None  # noqa S101
        return self._total

    def __len__(self) -> int:
        """Get the total number of items across all pages."""
        return self.total

    async def get(self, index: int) -> ResourceType:
        """Get an item by index."""
        if index < 0:
            raise IndexError(f"Negative indexing is not supported: {index}")
        await self._fetch_to_index(index)
        if index >= len(self._elements):
            raise IndexError(f"list index out of range: {index}")
        return self._elements[index]

    async def collect(self) -> list[ResourceType]:
        """Fetch all pages and return the full list of items."""
        while self._could_grow():
            await self._grow()
        return list(self._elements)

    def _could_grow(self) -> bool:
        return self._next_path is not None

    async def _grow(self) -> list[ResourceType]:
        new_elements = await self._fetch_next_page()
        self._elements.extend(new_elements)
        return new_elements

    async def _fetch_next_page(self) -> list[ResourceType]:
        assert self._next_path is not None  # noqa S101
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

    async def _fetch_to_index(self, index: int):
        while len(self._elements) <= index and self._could_grow():
            await self._grow()
