from __future__ import annotations

import datetime as dt
from typing import Any


class AsyncResource:
    """
    Base class for async resources.

    Mirrors the sync Resource but with async methods for
    traversing relations via the async client.
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
        """Convenient representation giving a preview of the item."""
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
                value = [i.as_dict() if isinstance(i, AsyncResource) else i for i in value]
            elif isinstance(value, AsyncResource):
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
        resource_type: type[AsyncResource] | None = None,
        params: dict | None = None,
        fwd_parent: bool = True,
    ):
        """
        Generic async method to load the relation from any resource.

        Query the client with the object's known parameters
        and try to retrieve the provided relation type.
        """
        return await self.client.request(
            "GET",
            f"{self.type}/{self.id}/{relation}",
            parent=self if fwd_parent else None,
            resource_type=resource_type,
            params=params,
        )
