from __future__ import annotations

import pytest

from deezer import Album, Artist, PaginatedList

pytestmark = pytest.mark.vcr


class TestPaginatedList:
    """Tests for the PaginatedList class."""

    @pytest.fixture()
    def daft_punk_albums(self, client):
        parent = Artist(client, {"id": 27, "type": "artist"})
        return PaginatedList(
            client=client,
            parent=parent,
            base_path="artist/27/albums",
        )

    def test_repr_many_results(self, daft_punk_albums):
        assert repr(daft_punk_albums) == (
            "<PaginatedList ["
            "<Album: Homework (25th Anniversary Edition)>, "
            "<Album: Human After All (Remixes)>, "
            "<Album: Random Access Memories>, "
            "<Album: TRON: Legacy Reconfigured>, "
            "<Album: TRON: Legacy - The Complete Edition (Original Motion Picture Soundtrack)>, "
            "'...'"
            "]>"
        )

    def test_repr_little_results(self, client):
        results = client.search_artists("rouquine")
        assert repr(results) == ("<PaginatedList [<Artist: Rouquine>, <Artist: Rouquined>]>")

    def test_repr_empty(self, client):
        results = client.search_artists("something very complicated without results")
        assert repr(results) == "<PaginatedList []>"

    def test_total(self, daft_punk_albums):
        assert daft_punk_albums.total == 32
        assert len(daft_punk_albums) == 32

    def test_iterate(self, daft_punk_albums):
        iter_count = 0
        for iter_count, album in enumerate(daft_punk_albums, 1):  # noqa B007
            assert isinstance(album, Album)
        assert iter_count == 32
        # This shouldn't do another API call
        assert daft_punk_albums.total == 32

    def test_iterator(self, daft_punk_albums):
        a1 = next(daft_punk_albums)
        a2 = next(daft_punk_albums)
        a3 = next(daft_punk_albums)

        assert a1.title == "Human After All (Remixes)"
        assert a2.title == "Random Access Memories"
        assert a3.title == "TRON: Legacy Reconfigured"

    @pytest.mark.parametrize(
        ("index", "title"),
        [
            (4, "Alive 2007"),
            (30, "One More Time"),
        ],
    )
    def test_get_element(self, daft_punk_albums, index, title):
        album = daft_punk_albums[index]
        assert isinstance(album, Album)
        assert album.title == title

    def test_get_element_index_error(self, daft_punk_albums):
        with pytest.raises(IndexError):
            daft_punk_albums[40]

    def test_get_element_negative_value(self, daft_punk_albums):
        with pytest.raises(IndexError):
            daft_punk_albums[-1]

    def test_slicing_simple(self, daft_punk_albums):
        albums = daft_punk_albums[5:8]
        assert [a.title for a in albums] == [
            "Musique, Vol. 1",
            "Human After All",
            "Daft Club",
        ]

    def test_slicing_no_start(self, daft_punk_albums):
        albums = daft_punk_albums[:3]
        assert [a.title for a in albums] == [
            "Human After All (Remixes)",
            "Random Access Memories",
            "TRON: Legacy Reconfigured",
        ]

    def test_slicing_no_end(self, daft_punk_albums):
        albums = daft_punk_albums[27:]
        assert [a.title for a in albums] == [
            "Something About Us (Love Theme from Interstella)",
            "Digital Love",
            "Aerodynamic",
            "One More Time",
            "Da Funk",
        ]

    def test_slicing_with_step(self, daft_punk_albums):
        albums = daft_punk_albums[2:10:2]
        assert [a.title for a in albums] == [
            "TRON: Legacy Reconfigured",
            "Alive 2007",
            "Human After All",
            "Alive 1997",
        ]

    def test_authenticated_requests(self, client_token):
        user_tracks = PaginatedList(
            client=client_token,
            base_path="user/me/tracks",
            params={"limit": 2},
        )
        assert [t.title for t in user_tracks] == [
            "Poney Pt. I",
            "Young Blood",
            "Flyover",
        ]
