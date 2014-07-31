import deezer
import unittest

from mock import patch


def mocked_get_object(dummy_inst, object_t,
                      object_id=None, dummy_relation=None):
    """
    Basic function to mock the get_object Client's method.
    Returns a json object, either with the id provided, or
    as list of id's in the data field of a json object.
    """
    if object_id:
        item = {
            "id": str(object_id),
            "type": object_t,
            "name": "foo",
            "related": {
                "id": "12",
                "name": "bar"
            }
        }
    else:
        item = {
            "data": [
                {
                    "id": "1",
                    "type": object_t,
                    "name": "foo",
                    "related": {
                        "id": "12",
                        "name": "bar"
                    }
                }
            ]
        }
    return item


class TestClient(unittest.TestCase):
    def setUp(self):
        self.patcher = patch('deezer.Client.get_object', mocked_get_object)
        self.patcher.start()
        self.client = deezer.Client(app_id='foo', app_secret='bar')
        self.unsec_client = deezer.Client(use_ssl=False)

    def tearDown(self):
        # pass
        self.patcher.stop()

    def test_kwargs_parsing_valid(self):
        """Test that valid kwargs are stored as properties on the client."""
        self.assertEqual(self.client.app_id, 'foo')
        self.assertEqual(self.client.app_secret, 'bar')

    def test_ssl(self):
        """Test that the ssl parameter provides the right scheme"""
        self.assertEqual(self.client.scheme, 'https')
        self.assertEqual(self.unsec_client.scheme, 'http')

    def test_output(self):
        """Test the ouput format requested"""
        self.assertEqual(self.client.output, "json")

    def test_url(self):
        """Test the url() method
        it should add / to the request if not present
        """
        self.client.url()
        user = self.client.url('/user')
        self.assertEqual(user, "https://api.deezer.com/user")
        user = self.client.url('user')
        self.assertEqual(user, "https://api.deezer.com/user")

    def test_object_url(self):
        """Test the object_url() method, validates against the allowed types
        of objects"""
        self.client.object_url("album")
        self.client.object_url("album", 12)
        album = self.client.object_url("album", "12")
        self.assertEqual(album, "https://api.deezer.com/album/12")
        self.assertRaises(TypeError, self.client.object_url, 'foo')

    def test_get_album(self):
        """Test method to retrieve an album"""
        album = self.client.get_album(12)
        self.assertIsInstance(album, deezer.resources.Album)

    def test_get_artist(self):
        """Test methods to get an artist"""
        artist = self.client.get_artist(12)
        self.assertIsInstance(artist, deezer.resources.Artist)

    def test_get_comment(self):
        """Test methods to get a comment"""
        comment = self.client.get_comment(12)
        self.assertIsInstance(comment, deezer.resources.Comment)

    def test_get_genre(self):
        """Test methods to get a genre"""
        genre = self.client.get_genre(1)
        self.assertIsInstance(genre, deezer.resources.Genre)

    def test_get_genres(self):
        """Test methods to get several genres"""
        genres = self.client.get_genres()
        self.assertIsInstance(genres, list)
        self.assertIsInstance(genres[0], deezer.resources.Genre)

    def test_get_playlist(self):
        """Test methods to get a playlist"""
        playlist = self.client.get_playlist(1)
        self.assertIsInstance(playlist, deezer.resources.Playlist)

    def test_get_radio(self):
        """Test methods to get a radio"""
        radio = self.client.get_radio(1)
        self.assertIsInstance(radio, deezer.resources.Radio)

    def test_get_track(self):
        """Test methods to get a track"""
        track = self.client.get_track(1)
        self.assertIsInstance(track, deezer.resources.Track)

    def test_get_user(self):
        """Test methods to get a user"""
        user = self.client.get_user(1)
        self.assertIsInstance(user, deezer.resources.User)


if __name__ == '__main__':
    unittest.main()
