from deezer.client import Client
from deezer.pagination import PaginatedList
from deezer.resources import (
    Album,
    Artist,
    Genre,
    Playlist,
    Radio,
    Resource,
    Track,
    User,
)

__version__ = "4.3.0"
__all__ = [
    "Client",
    "PaginatedList",
    "Resource",
    "Album",
    "Artist",
    "Genre",
    "Playlist",
    "Track",
    "User",
    "Radio",
]

USER_AGENT = f"Deezer Python API Wrapper v{__version__}"
