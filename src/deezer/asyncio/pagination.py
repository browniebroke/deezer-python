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
        self.__elements: list[ResourceType] = []
        self.__client = client
        self.__base_path = base_path
        self.__base_params = params or {}
        self.__next_path: str | None = base_path
        self.__next_params = params or {}
        self.__parent = parent
        self.__total: int | None = None
        self.__iter_index = 0

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
        data: list[ResourceType | str] = list(self.__elements[: repr_size + 1])
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
            if yield_index < len(self.__elements):
                yield self.__elements[yield_index]
                yield_index += 1
            elif self._could_grow():
                await self._grow()
            else:
                break

    async def __anext__(self) -> ResourceType:
        """Get the next item from the list."""
        if self.__iter_index < len(self.__elements):
            item = self.__elements[self.__iter_index]
            self.__iter_index += 1
            return item
        if self._could_grow():
            new_elements = await self._grow()
            if new_elements and self.__iter_index < len(self.__elements):
                item = self.__elements[self.__iter_index]
                self.__iter_index += 1
                return item
        raise StopAsyncIteration

    @property
    def total(self) -> int:
        """The total number of items in the list, mirroring what Deezer returns."""
        assert self.__total is not None  # noqa S101
        return self.__total

    def __len__(self) -> int:
        """Get the total number of items across all pages."""
        return self.total

    async def get(self, index: int) -> ResourceType:
        """Get an item by index."""
        if index < 0:
            raise IndexError(f"Negative indexing is not supported: {index}")
        await self._fetch_to_index(index)
        if index >= len(self.__elements):
            raise IndexError(f"list index out of range: {index}")
        return self.__elements[index]

    async def collect(self) -> list[ResourceType]:
        """Fetch all pages and return the full list of items."""
        while self._could_grow():
            await self._grow()
        return list(self.__elements)

    def _could_grow(self) -> bool:
        return self.__next_path is not None

    async def _grow(self) -> list[ResourceType]:
        new_elements = await self._fetch_next_page()
        self.__elements.extend(new_elements)
        return new_elements

    async def _fetch_next_page(self) -> list[ResourceType]:
        assert self.__next_path is not None  # noqa S101
        response_payload = await self.__client.request(
            "GET",
            self.__next_path,
            parent=self.__parent,
            paginate_list=True,
            params=self.__next_params,
        )
        self.__next_path = None
        self.__total = response_payload.get("total")
        next_url = response_payload.get("next", None)
        if next_url:
            url_bits = urlparse(next_url)
            self.__next_path = url_bits.path.lstrip("/")
            self.__next_params = parse_qs(url_bits.query)
        return response_payload["data"]

    async def _fetch_to_index(self, index: int):
        while len(self.__elements) <= index and self._could_grow():
            await self._grow()
