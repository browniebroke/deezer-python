from __future__ import annotations

from typing import Any, ClassVar

from deezer.exceptions import DeezerUnknownResource
from deezer.resources import (
    Album,
    Artist,
    Chart,
    Editorial,
    Episode,
    Genre,
    Playlist,
    Podcast,
    Radio,
    Resource,
    Track,
    User,
)


class DeezerMixin:
    """Mixin providing shared logic for both sync and async Deezer clients."""

    _resource_base_class: ClassVar[type[Resource]] = Resource

    objects_types: ClassVar[dict[str, type[Resource] | None]] = {
        "album": Album,
        "artist": Artist,
        "chart": Chart,
        "editorial": Editorial,
        "episode": Episode,
        "genre": Genre,
        "playlist": Playlist,
        "podcast": Podcast,
        "radio": Radio,
        "search": None,
        "track": Track,
        "user": User,
    }

    def _process_json(
        self,
        item: dict[str, Any],
        parent: Resource | None = None,
        resource_type: type[Resource] | None = None,
        resource_id: int | None = None,
        paginate_list=False,
    ):
        """
        Recursively convert dictionary to :class:`~deezer.Resource` object.

        :param item: the JSON response as dict.
        :param parent: A reference to the parent resource, to avoid fetching again.
        :param resource_type: The resource class to use as top level.
        :param resource_id: The resource id to use as top level.
        :param paginate_list: Whether to wrap list into a pagination object.
        :returns: instance of :class:`~deezer.Resource`
        """
        if "data" in item:
            parsed_data = [self._process_json(i, parent, paginate_list=False) for i in item["data"]]
            if not paginate_list:
                return parsed_data
            item["data"] = parsed_data
            return item

        result = {}
        for key, value in item.items():
            if isinstance(value, dict) and ("type" in value or "data" in value):
                value = self._process_json(value, parent)
            result[key] = value
        if parent is not None:
            result[parent.type] = parent

        if "id" not in result and resource_id is not None:
            result["id"] = resource_id

        if "type" in result and result["type"] in self.objects_types:
            object_class = self.objects_types[result["type"]]
        elif "type" in result or (not resource_type and "id" in result):
            object_class = self._resource_base_class
        elif resource_type:
            object_class = resource_type
        elif item.get("results") is True:
            return True
        else:
            raise DeezerUnknownResource(f"Unable to find resource type for {result!r}")
        assert object_class is not None  # noqa S101
        return object_class(self, result)
