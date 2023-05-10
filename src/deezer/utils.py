from __future__ import annotations

from typing import TYPE_CHECKING, Generator, Iterable

if TYPE_CHECKING:
    from deezer import Resource


def gen_ids(item_list: Iterable[int | Resource]) -> Generator[int, None, None]:
    """Get IDs for an iterable of `int` or `Resources`."""
    for item in item_list:
        yield get_id(item)


def get_id(item: int | Resource) -> int:
    """Get ID for an `int` or `Resource`."""
    if isinstance(item, int):
        return item
    if hasattr(item, "id"):
        return item.id
    raise NotImplementedError(f"Unknown type for {item}")
