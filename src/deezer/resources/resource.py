from __future__ import annotations

import datetime as dt
from typing import Any

from ..pagination import PaginatedList

NOT_INFERRED = object()


class Resource:
    """
    Base class for any resource.

    It is mainly responsible for passing a reference to the client
    to this class when instantiated, and transmit the json data into
    attributes
    """

    id: int
    type: str

    _fields: tuple[str, ...]
    _fetched: bool

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

    def get_relation(self, relation, **kwargs):
        """
        Generic method to load the relation from any resource.

        Query the client with the object's known parameters
        and try to retrieve the provided relation type. This
        is not meant to be used directly by a client, it's more
        a helper method for the child objects.
        """
        return self.client.request(
            "GET",
            f"{self.type}/{self.id}/{relation}",
            parent=self,
            **kwargs,
        )

    def get_paginated_list(
        self,
        relation: str,
        **kwargs,
    ):
        return PaginatedList(
            client=self.client,
            base_path=f"{self.type}/{self.id}/{relation}",
            parent=self,
            **kwargs,
        )

    def __getattr__(self, item: str) -> Any:
        """
        Called when the default attribute access fails with an AttributeError.

        This is a fallback method, not need to call the parent implementation.
        If the attribute is found through the normal mechanism, this is NOT called.
        """
        class_annotations = self.__class__.__annotations__
        if item in class_annotations:
            result = self._infer_missing_field(item)
            if result is not NOT_INFERRED:
                setattr(self, item, result)
                self._fields += (item,)
                return result
            elif not getattr(self, "_fetched", False):
                full_resource = self.get()
                missing_fields = set(full_resource._fields) - set(self._fields)
                for field_name in missing_fields:
                    setattr(self, field_name, getattr(full_resource, field_name))
                    self._fields += (field_name,)
                return getattr(self, item)
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{item}'"
        )

    def _infer_missing_field(self, item: str) -> Any:
        """
        Hook to infer missing field values.

        To be implemented in the subclasses for concrete resources.
        """
        return NOT_INFERRED

    def get(self):
        """Get the resource from the API."""
        self._fetched = True
        return self.client.request("GET", f"{self.type}/{self.id}")
