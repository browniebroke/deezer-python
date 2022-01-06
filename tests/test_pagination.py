import pytest

from deezer import Album, Artist, PaginatedList

pytestmark = pytest.mark.vcr


class TestPaginatedList:
    def test_total(self, client):
        container = Artist(client, {"id": 27, "type": "artist"})
        paginated = PaginatedList(container=container, base_path="artist/27/albums")
        assert paginated.total == 32

    def test_iterate(self, client):
        container = Artist(client, {"id": 27, "type": "artist"})
        paginated = PaginatedList(container=container, base_path="artist/27/albums")
        iter_count = 0
        for iter_count, album in enumerate(paginated, 1):
            assert isinstance(album, Album)
        assert iter_count == 32

    @pytest.mark.parametrize(
        ("index", "title"),
        [
            (2, "TRON: Legacy Reconfigured"),
            (30, "One More Time"),
        ],
    )
    def test_get_element(self, client, index, title):
        container = Artist(client, {"id": 27, "type": "artist"})
        paginated = PaginatedList(container=container, base_path="artist/27/albums")
        album = paginated[index]
        assert isinstance(album, Album)
        assert album.title == title

    def test_get_element_index_error(self, client):
        container = Artist(client, {"id": 27, "type": "artist"})
        paginated = PaginatedList(container=container, base_path="artist/27/albums")
        with pytest.raises(IndexError):
            paginated[40]
