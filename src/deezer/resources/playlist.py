from __future__ import annotations

from typing import TYPE_CHECKING

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

    def add_tracks(self, tracks: list, **kwargs) -> bool:
        """
        Add tracks to a playlist.

        :param tracks: A list of the track's or track id's to add to the playlist
        :returns: a boolean that tells if the operation was successful
        """
        tracks_ids = []
        for track in tracks:
            if isinstance(track, int):
                tracks_ids.append(str(track))
            else:
                tracks_ids.append(str(track.id))
        tracks_parsed = ",".join(tracks_ids)
        return self.client.request(
            "POST", f"playlist/{self.id}/tracks", songs=tracks_parsed, **kwargs
        )

    def delete_tracks(self, tracks: list, **kwargs) -> bool:
        """
        Delete tracks from a playlist.

        :param tracks: A list of the track's or track id's to delete to the playlist
        :returns: a boolean that tells if the operation was successful
        """
        tracks_ids = []
        for track in tracks:
            if isinstance(track, int):
                tracks_ids.append(str(track))
            else:
                tracks_ids.append(str(track.id))
        tracks_parsed = ",".join(tracks_ids)
        return self.client.request(
            "DELETE", f"playlist/{self.id}/tracks", songs=tracks_parsed, **kwargs
        )

    def reorder_tracks(self, order: list[int], **kwargs) -> bool:
        """
        Reorder the tracks of a playlist.

        :param order: A list of the track id's in the wished order
        :returns: a boolean that tells if the operation was successful
        """
        order_string = ",".join(map(str, order))
        return self.client.request(
            "POST", f"playlist/{self.id}/tracks", order=order_string, **kwargs
        )
