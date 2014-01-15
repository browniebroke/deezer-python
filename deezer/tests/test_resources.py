import deezer
import unittest


class TestResources(unittest.TestCase):

    def test_album_attributes(self):
        client = deezer.Client()
        album = client.get_album(12)
        self.assertTrue(hasattr(album, 'title'))