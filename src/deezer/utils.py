from __future__ import annotations

from typing import TYPE_CHECKING, Generator, Iterable

if TYPE_CHECKING:
    from deezer import Resource


def gen_ids(item_list: Iterable[int | Resource]) -> Generator[int, None, None]:
    """Get IDs for an iterable of `int` or `Resources`."""
    for item in item_list:
        if isinstance(item, int):
            yield item
        elif hasattr(item, "id"):
            yield item.id
        else:
            raise NotImplementedError(f"Unknown type for {item}")
