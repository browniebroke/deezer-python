from typing import Type, List

import deezer


class PaginatedList:
    """
    This class abstracts paginated list from the API.

    You can simply enumerate through instances of this class::
        for album in artist.get_albums():
            print(album.title)

    If you want to know the total number of items in the list::
        print(artist.get_albums().total)
    """

    # Lifted and adapted from PyGithub:
    # https://github.com/PyGithub/PyGithub/blob/master/github/PaginatedList.py

    # TODO: check if possible with REST API:
    #
    # You can also index them or take slices::
    #     second_album = artist.get_albums()[1]
    #     first_ten_albums = artist.get_albums()[:10]
    #
    # If you want to iterate in reversed order, just do::
    #     for album in artist.get_albums().reversed:
    #         print(album.title)
    #
    # And if you really need it, you can explicitly access a specific page::
    #     some_albums = artist.get_albums().get_page(0)
    #     some_other_albums = user.get_albums().get_page(3)

    def __init__(
        self,
        container: "deezer.Resource",
        resource_class: Type["deezer.Resource"],
        base_path: str,
        **params,
    ):
        self.__elements: List["deezer.Resource"] = []
        self.__container = container
        self.__client = container.client
        self.__resource_class = resource_class
        self.__base_path = base_path
        self.__params = params
        self.__next_path = base_path
        self.__total = None

    def __iter__(self):
        yield from self.__elements
        while self._could_grow():
            yield from self._grow()

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
            parent=self.__container,
            **self.__params,
        )
        data = response_payload["data"]
        self.__next_path = None

        if data:
            next_url = response_payload.get("next", None)
            self.__next_path = (
                next_url.replace(f"{self.__client.base_url}/", "") if next_url else None
            )
        return data

    @property
    def total(self) -> int:
        if self.__total is None:
            params = self.__params.copy()
            params["limit"] = 1
            response_payload = self.__client.request(
                "GET",
                self.__base_path,
                parent=self.__container,
                **params,
            )
            self.__total = response_payload["total"]
        return self.__total
