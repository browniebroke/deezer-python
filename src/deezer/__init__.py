from deezer.client import Client
from deezer.pagination import PaginatedList
from deezer.resources import (
    Album,
    Artist,
    Editorial,
    Genre,
    Playlist,
    Radio,
    Resource,
    Track,
    User,
)

__version__ = "5.2.0"
__all__ = [
    "Client",
    "PaginatedList",
    "Resource",
    "Album",
    "Artist",
    "Editorial",
    "Genre",
    "Playlist",
    "Track",
    "User",
    "Radio",
]

USER_AGENT = f"Deezer Python API Wrapper v{__version__}"
