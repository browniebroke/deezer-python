from __future__ import annotations

from typing import TYPE_CHECKING, Iterable

from ..utils import gen_ids
from .resource import Resource

if TYPE_CHECKING:
    from ..pagination import PaginatedList
    from .track import Track
    from .user import User


class Playlist(Resource):
    """
    To work with Deezer playlist objects.

    Check the :deezer-api:`Deezer documentation <playlist>`
    for more details about each field.
    """

    id: int
    title: str
    description: str
    duration: int
    public: bool
    is_loved_track: bool
    collaborative: bool
    nb_tracks: int
    unseen_track_count: int
    fans: int
    link: str
    share: str
    picture: str
    picture_small: str
    picture_medium: str
    picture_big: str
    picture_xl: str
    checksum: str
    creator: User
    tracks: list[Track]

    def get_tracks(self, **kwargs) -> PaginatedList[Track]:
        """
        Get tracks from a playlist.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`Track <deezer.Track>` instances
        """
        return self.get_paginated_list("tracks", **kwargs)

    def get_fans(self, **kwargs) -> PaginatedList[User]:
        """
        Get fans from a playlist.

        :returns: a :class:`PaginatedList <deezer.PaginatedList>`
                  of :class:`User <deezer.User>` instances
        """
        return self.get_paginated_list("fans", **kwargs)

    def mark_seen(self, **kwargs) -> bool:
        """
        Mark the playlist as seen.

        :returns: a boolean that tells if the operation was successful
        """
        return self.client.request("POST", f"playlist/{self.id}/seen", **kwargs)

    def add_tracks(self, tracks: Iterable[int | Track], **kwargs) -> bool:
        """
        Add tracks to a playlist.

        :param tracks: An iterable of :class:`Track <deezer.Track>` instances
                       or their IDs to add to the playlist
        :returns: a boolean that tells if the operation was successful
        """
        track_ids_str = ",".join(str(tid) for tid in gen_ids(tracks))
        return self.client.request(
            "POST", f"playlist/{self.id}/tracks", songs=track_ids_str, **kwargs
        )

    def delete_tracks(self, tracks: Iterable[int | Track], **kwargs) -> bool:
        """
        Delete tracks from a playlist.

        :param tracks: An iterable of :class:`Track <deezer.Track>` instances
                       or their IDs to remove from the playlist.
        :returns: a boolean that tells if the operation was successful
        """
        track_ids_str = ",".join(map(str, gen_ids(tracks)))
        return self.client.request(
            "DELETE", f"playlist/{self.id}/tracks", songs=track_ids_str, **kwargs
        )

    def reorder_tracks(self, order: Iterable[int | Track], **kwargs) -> bool:
        """
        Reorder the tracks of a playlist.

        :param order: An iterable of :class:`Track <deezer.Track>` instances
                      or their IDs in the wished order.
        :returns: a boolean that tells if the operation was successful
        """
        order_track_ids_str = ",".join(map(str, gen_ids(order)))
        return self.client.request(
            "POST", f"playlist/{self.id}/tracks", order=order_track_ids_str, **kwargs
        )
