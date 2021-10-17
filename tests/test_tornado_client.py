import pytest
from tornado.httpclient import AsyncHTTPClient

from deezer import Album
from deezer.contrib.tornado import AsyncClient

pytestmark = pytest.mark.vcr


class TestAsyncClient:
    @pytest.fixture()
    def async_client(self):
        return AsyncClient()

    @pytest.mark.gen_test
    def test_access_token_set(self, async_client, mocker):
        client_fetch = mocker.spy(AsyncHTTPClient, "fetch")
        async_client.access_token = "dummy"
        yield async_client.request("GET", "user/me")
        client_fetch.assert_called_with(
            mocker.ANY,
            "https://api.deezer.com/user/me?access_token=dummy",
            method="GET",
        )

    @pytest.mark.gen_test
    def test_get_object(self, async_client):
        album = yield async_client.get_album(302127)
        assert isinstance(album, Album)

    @pytest.mark.gen_test
    def test_get_relation(self, async_client):
        album = Album(async_client, {"id": 302127, "type": "album"})
        tracks = yield album.get_tracks()
        assert tracks[0].album is album
