from __future__ import annotations

from typing import Generator, Generic, TypeVar, overload
from urllib.parse import parse_qs, urlparse

import deezer

ResourceType = TypeVar("ResourceType")
REPR_OUTPUT_SIZE = 5


class PaginatedList(Generic[ResourceType]):
    """Abstract paginated response from the API and make them more Pythonic."""

    # Lifted and adapted from PyGithub:
    # https://github.com/PyGithub/PyGithub/blob/master/github/PaginatedList.py

    def __init__(
        self,
        client: deezer.Client,
        base_path: str,
        parent: deezer.Resource | None = None,
        **params,
    ):
        self.__elements: list[ResourceType] = []
        self.__client = client
        self.__base_path = base_path
        self.__base_params = params
        self.__next_path: str | None = base_path
        self.__next_params = params
        self.__parent = parent
        self.__total = None
        self.__iter = iter(self)

    def __repr__(self) -> str:
        """Convenient representation giving a preview of the content."""
        repr_size = 5
        data: list[ResourceType | str] = list(self[: repr_size + 1])
        if len(data) > repr_size:
            data[-1] = "..."
        return f"<{self.__class__.__name__} {data!r}>"

    @overload
    def __getitem__(self, index: int) -> ResourceType:
        ...

    @overload
    def __getitem__(self, index: slice) -> list[ResourceType]:
        ...

    def __getitem__(
        self,
        index: int | slice,
    ) -> ResourceType | list[ResourceType]:
        """Get an item or a slice of items from the list."""
        if isinstance(index, int):
            self._fetch_to_index(index)
            return self.__elements[index]
        if index.stop is not None:
            self._fetch_to_index(index.stop)
        else:
            while self._could_grow():
                self._grow()
        return self.__elements[index]

    def __iter__(self) -> Generator[ResourceType, None, None]:
        """Iterate over the internal, fetching new pages as needed."""
        yield from self.__elements
        while self._could_grow():
            yield from self._grow()

    def __next__(self) -> ResourceType:
        """Get the next item from the list."""
        return next(self.__iter)

    def __len__(self) -> int:
        """Get the total number of items across all pages."""
        return self.total

    def _could_grow(self) -> bool:
        return self.__next_path is not None

    def _grow(self) -> list[ResourceType]:
        new_elements = self._fetch_next_page()
        self.__elements.extend(new_elements)
        return new_elements

    def _fetch_next_page(self) -> list[ResourceType]:
        assert self.__next_path is not None  # noqa S101
        response_payload = self.__client.request(
            "GET",
            self.__next_path,
            parent=self.__parent,
            paginate_list=True,
            **self.__next_params,
        )
        self.__next_path = None
        self.__total = response_payload.get("total")
        next_url = response_payload.get("next", None)
        if next_url:
            url_bits = urlparse(next_url)
            self.__next_path = url_bits.path.lstrip("/")
            self.__next_params = parse_qs(url_bits.query)
        return response_payload["data"]

    def _fetch_to_index(self, index: int):
        while len(self.__elements) <= index and self._could_grow():
            self._grow()

    @property
    def total(self) -> int:
        """The total number of items in the list, mirroring what Deezer returns."""
        if self.__total is None:
            params = self.__base_params.copy()
            params["limit"] = 1
            response_payload = self.__client.request(
                "GET",
                self.__base_path,
                parent=self.__parent,
                paginate_list=True,
                **params,
            )
            self.__total = response_payload["total"]
        assert self.__total is not None  # noqa S101
        return self.__total
