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

    def test_total(self, daft_punk_albums):
        assert daft_punk_albums.total == 32

    def test_iterate(self, daft_punk_albums):
        iter_count = 0
        for iter_count, album in enumerate(daft_punk_albums, 1):
            assert isinstance(album, Album)
        assert iter_count == 32
        # This shouldn't do another API call
        assert daft_punk_albums.total == 32

    @pytest.mark.parametrize(
        ("index", "title"),
        [
            (2, "TRON: Legacy Reconfigured"),
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

    def test_authenticated_requests(self, client_token):
        user_tracks = PaginatedList(
            client=client_token,
            base_path="user/me/tracks",
            limit=2,
        )
        assert [t.title for t in user_tracks] == [
            "Poney Pt. I",
            "Young Blood",
            "Flyover",
        ]
