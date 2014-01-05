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
        u = self.client.url('/user')
        self.assertEqual(u, "https://api.deezer.com/user")
        self.assertRaises(Exception, self.client.url, 'user')

    def test_object_url(self):
        """Test the object_url() method, validates against the allowed types
        of objects"""
        self.client.object_url("album")
        self.client.object_url("album", 12)
        a = self.client.object_url("album", "12")
        self.assertEqual(a, "https://api.deezer.com/album/12")
        self.assertRaises(TypeError, self.client.object_url, 'foo')

    def test_get_album(self):
        """Test object() method"""
        expected = {u'available': False, u'rating': 0, u'nb_tracks': 0, u'title': u'Monkey Business', u'tracks': {u'data': []}, u'release_date': u'0000-00-00', u'artist': {u'picture': u'https://api.deezer.com/artist/12/image', u'id': 12, u'name': u'Black Eyed Peas'}, u'cover': u'https://api.deezer.com/album/12/image', u'upc': u'_0602498822289', u'label': u'Universal Music Division Polydor', u'fans': 5, u'link': u'http://www.deezer.com/album/12', u'duration': 0, u'type': u'album', u'id': 12, u'genre_id': 18}
        value = self.client.get_album(12)
        self.assertEqual(value, expected)

    def test_get_album_xml(self):
        expected = '<?xml version="1.0" encoding="utf-8"?><root><id><![CDATA[12]]></id><title><![CDATA[Monkey Business]]></title><upc><![CDATA[_0602498822289]]></upc><link><![CDATA[http://www.deezer.com/album/12]]></link><cover><![CDATA[http://api.deezer.com/album/12/image]]></cover><genre_id><![CDATA[18]]></genre_id><label><![CDATA[Universal Music Division Polydor]]></label><nb_tracks><![CDATA[0]]></nb_tracks><duration><![CDATA[0]]></duration><fans><![CDATA[5]]></fans><rating><![CDATA[0]]></rating><release_date><![CDATA[0000-00-00]]></release_date><available><![CDATA[]]></available><artist><id><![CDATA[12]]></id><name><![CDATA[Black Eyed Peas]]></name><picture><![CDATA[http://api.deezer.com/artist/12/image]]></picture></artist><type><![CDATA[album]]></type><tracks><data></data></tracks></root>'
        value = self.undef_client.get_album(12)
        self.assertEqual(value, expected)


if __name__ == '__main__':
    unittest.main()