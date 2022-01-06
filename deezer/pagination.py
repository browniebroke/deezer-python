from typing import List, Optional
from urllib.parse import parse_qs, urlparse

import deezer


class PaginatedList:
    """
    This class abstracts paginated list from the API.

    You can simply enumerate through instances of this class::
        for album in artist.get_albums():
            print(album.title)

    If you want to know the total number of items in the list::
        print(artist.get_albums().total)
        len(artist.get_albums())

    You can also index them::
        second_album = artist.get_albums()[1]
    """

    # Lifted and adapted from PyGithub:
    # https://github.com/PyGithub/PyGithub/blob/master/github/PaginatedList.py

    def __init__(
        self,
        client: "deezer.Client",
        base_path: str,
        parent: Optional["deezer.Resource"] = None,
        **params,
    ):
        self.__elements: List["deezer.Resource"] = []
        self.__client = client
        self.__base_path = base_path
        self.__base_params = params
        self.__next_path = base_path
        self.__next_params = params
        self.__parent = parent
        self.__total = None

    def __getitem__(self, index: int) -> "deezer.Resource":
        self._fetch_to_index(index)
        return self.__elements[index]

    def __iter__(self):
        yield from self.__elements
        while self._could_grow():
            yield from self._grow()

    def __len__(self):
        return self.total

    def _could_grow(self):
        return self.__next_path is not None

    def _grow(self):
        new_elements = self._fetch_next_page()
        self.__elements.extend(new_elements)
        return new_elements

    def _fetch_next_page(self):
        response_payload = self.__client.request(
            "GET",
            self.__next_path,
            parent=self.__parent,
            paginate_list=True,
            **self.__next_params,
        )
        data = response_payload["data"]
        self.__next_path = None

        if data:
            self.__total = response_payload.get("total")
            next_url = response_payload.get("next", None)
            if next_url:
                url_bits = urlparse(next_url)
                self.__next_path = url_bits.path.lstrip("/")
                self.__next_params = parse_qs(url_bits.query)
        return data

    def _fetch_to_index(self, index: int):
        while len(self.__elements) <= index and self._could_grow():
            self._grow()

    @property
    def total(self) -> int:
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
        return self.__total
