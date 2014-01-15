import deezer
import unittest


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = deezer.Client(app_id='foo', app_secret='bar')
        self.undef_client = deezer.Client(app_id='foo', app_secret='bar',
                                          use_ssl=False, output='xml')

    def test_kwargs_parsing_valid(self):
        """Test that valid kwargs are stored as properties on the client."""
        self.assertEqual(self.client.app_id, 'foo')
        self.assertEqual(self.client.app_secret, 'bar')

    def test_ssl(self):
        """Test that the ssl parameter provides the right scheme"""
        self.assertEqual(self.client.scheme, 'https://')
        self.assertEqual(self.undef_client.scheme, 'http://')

    def test_output(self):
        """Test the ouput format requested"""
        self.assertEqual(self.client.output, "json")
        self.assertEqual(self.undef_client.output, "xml")

    def test_url(self):
        """Test the url() method
        it should add / to the request if not present
        """
        self.client.url()
        user = self.client.url('/user')
        self.assertEqual(user, "https://api.deezer.com/user")
        self.assertRaises(ValueError, self.client.url, 'user')

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
        self.assertEqual(album.title, 'Monkey Business')

    def test_get_artist(self):
        """Test methods to get an artist"""
        artist = self.client.get_artist(12)
        self.assertIsInstance(artist, deezer.resources.Artist)
        self.assertEqual(artist.name, 'Black Eyed Peas')

        album = self.client.get_album(12)
        artist = album.get_artist()
        self.assertIsInstance(artist, deezer.resources.Artist)
        self.assertEqual(artist.name, 'Black Eyed Peas')


if __name__ == '__main__':
    unittest.main()