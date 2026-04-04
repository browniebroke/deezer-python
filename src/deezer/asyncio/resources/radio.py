from __future__ import annotations

from .resource import AsyncResource


class AsyncRadio(AsyncResource):
    """Async radio resource."""

    id: int
    title: str
    description: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    tracklist: str
    md5_image: str

    async def get_tracks(self) -> list:
        """Get first 40 tracks in the radio."""
        return await self.get_relation("tracks")
