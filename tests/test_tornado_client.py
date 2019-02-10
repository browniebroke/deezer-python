# -*- coding: utf-8
import tornado.gen
import tornado.ioloop

from deezer import Album
from deezer.contrib.tornado import AsyncClient
from .base import BaseTestCase


class TestAsyncClient(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.client = AsyncClient()

    def test_get_object(self):
        @tornado.gen.coroutine
        def callback():
            album = yield self.client.get_album(302127)
            self.assertIsInstance(album, Album)
            tracks = yield album.get_tracks()
            self.assertTrue(tracks[0].album is album)

        tornado.ioloop.IOLoop.instance().run_sync(callback)
