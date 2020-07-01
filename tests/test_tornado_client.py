import pytest
import tornado.gen
import tornado.ioloop

from deezer import Album
from deezer.contrib.tornado import AsyncClient

pytestmark = pytest.mark.vcr


class TestAsyncClient:
    def test_get_object(self):
        client = AsyncClient()

        @tornado.gen.coroutine
        def callback():
            album = yield client.get_album(302127)
            assert isinstance(album, Album)
            tracks = yield album.get_tracks()
            assert tracks[0].album is album

        tornado.ioloop.IOLoop.instance().run_sync(callback)
