from __future__ import annotations

import datetime as dt
from typing import Any

from async_deezer.pagination import AsyncPaginatedList
from deezer.resources import Resource as SyncResource


class Resource:
    """
    Async base class for any Deezer resource.

    This mirrors :class:`deezer.resources.Resource`, but relation helpers and
    ``get`` are implemented as async methods, and pagination returns
    :class:`async_deezer.pagination.AsyncPaginatedList`.
    """

    id: int
    type: str

    _fields: tuple[str, ...]

    def __init__(self, client, json):
        self.client = client
        for field_name in json.keys():
            parse_func = getattr(self, f"_parse_{field_name}", None)
            if callable(parse_func):
                json[field_name] = parse_func(json[field_name])
        self._fields = tuple(json.keys())
        for key in json:
            setattr(self, key, json[key])

    def __repr__(self):
        name = getattr(self, "name", None)
        title = getattr(self, "title", None)
        id_ = getattr(self, "id", None)
        return f"<{self.__class__.__name__}: {name or title or id_}>"

    def as_dict(self) -> dict[str, Any]:
        """Convert resource to dictionary."""
        result = {}
        for key in self._fields:
            value = getattr(self, key)
            if isinstance(value, list):
                value = [i.as_dict() if isinstance(i, Resource) else i for i in value]
            elif isinstance(value, Resource):
                value = value.as_dict()
            elif isinstance(value, dt.datetime):
                value = f"{value:%Y-%m-%d %H:%M:%S}"
            elif isinstance(value, dt.date):
                value = value.isoformat()
            result[key] = value
        return result

    async def get_relation(
        self,
        relation: str,
        resource_type: type["Resource"] | None = None,  # type: ignore[valid-type]
        params: dict | None = None,
        fwd_parent: bool = True,
    ):
        """
        Generic async method to load the relation from any resource.
        """
        return await self.client.request(
            "GET",
            f"{self.type}/{self.id}/{relation}",
            parent=self if fwd_parent else None,
            resource_type=resource_type,
            params=params,
        )

    async def post_relation(self, relation: str, params: dict):
        """
        Generic async method to make a POST request to a relation.
        """
        return await self.client.request(
            "POST",
            f"{self.type}/{self.id}/{relation}",
            params=params,
        )

    async def delete_relation(self, relation: str, params: dict | None = None):
        """
        Generic async method to make a DELETE request to a relation.
        """
        return await self.client.request(
            "DELETE",
            f"{self.type}/{self.id}/{relation}",
            params=params,
        )

    def get_paginated_list(
        self,
        relation: str,
        params: dict | None = None,
    ) -> AsyncPaginatedList:
        """
        Build the async pagination object based on the relation.

        Note that constructing the pagination object is synchronous
        network I/O only occurs when you iterate it or use its async helpers.
        """
        return AsyncPaginatedList(
            client=self.client,
            base_path=f"{self.type}/{self.id}/{relation}",
            parent=self,
            params=params,
        )

    def _infer_missing_field(self, item: str) -> Any:
        """
        Hook to infer missing field values, delegating to the sync base class
        to keep behavior consistent (e.g. inferred ``link`` / ``share``).
        """
        return SyncResource._infer_missing_field(self, item)

    def __getattr__(self, item: str) -> Any:
        """
        Fallback attribute access mirroring the synchronous Resource behavior.
        """
        return SyncResource.__getattr__(self, item)

    async def get(self):
        """Get the resource from the API."""
        return await self.client.request("GET", f"{self.type}/{self.id}")