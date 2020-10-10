from deezer.client import Client
from deezer.resources import (
    Album,
    Artist,
    Comment,
    Genre,
    Playlist,
    Radio,
    Resource,
    Track,
    User,
)

__version__ = "2.1.0"
__all__ = [
    "Client",
    "Resource",
    "Album",
    "Artist",
    "Genre",
    "Playlist",
    "Track",
    "User",
    "Comment",
    "Radio",
]

USER_AGENT = "Deezer Python API Wrapper v{}".format(__version__)
