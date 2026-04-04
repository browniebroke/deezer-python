from __future__ import annotations

from typing import TYPE_CHECKING

from .resource import AsyncResource

if TYPE_CHECKING:
    from .album import AsyncAlbum


class AsyncArtist(AsyncResource):
    """To work with async Deezer artist objects."""

    id: int
    name: str
    link: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    nb_album: int
    nb_fan: int
    radio: bool
    tracklist: str

    async def get_top(self, **kwargs) -> list:
        """Get the top tracks of an artist."""
        return await self.get_relation("top", **kwargs)

    async def get_related(self, **kwargs) -> list[AsyncArtist]:
        """Get a list of related artists."""
        return await self.get_relation("related", **kwargs)

    async def get_radio(self, **kwargs) -> list:
        """Get a list of tracks."""
        return await self.get_relation("radio", fwd_parent=False, **kwargs)

    async def get_albums(self, **kwargs) -> list[AsyncAlbum]:
        """Get a list of artist's albums."""
        return await self.get_relation("albums", **kwargs)

    async def get_playlists(self, **kwargs) -> list:
        """Get a list of artist's playlists."""
        return await self.get_relation("playlists", **kwargs)
