# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from types import GeneratorType

import deezer
from deezer.tests.base import BaseTestCase


class TestResources(BaseTestCase):
    def test_resource_relation(self):
        """
        Test passing parent object when using get_relation
        """
        client = deezer.Client()
        album = client.get_album(302127)
        tracks = album.get_tracks()
        self.assertTrue(tracks[0].album is album)

    def test_album_attributes(self):
        """
        Test album resource
        """
        client = deezer.Client()
        album = client.get_album(302127)
        self.assertTrue(hasattr(album, 'title'))
        self.assertEqual(repr(album), '<Album: Discovery>')
        artist = album.get_artist()
        self.assertIsInstance(artist, deezer.resources.Artist)
        self.assertEqual(repr(artist), '<Artist: Daft Punk>')

    def test_album_tracks(self):
        """
        Test tracks method of album resource
        """
        client = deezer.Client()
        album = client.get_album(302127)
        tracks = album.get_tracks()
        self.assertIsInstance(tracks, list)
        track = tracks[0]
        self.assertIsInstance(track, deezer.resources.Track)
        self.assertEqual(repr(track), '<Track: One More Time>')
        self.assertEqual(type(album.iter_tracks()), GeneratorType)
        track = list(album.iter_tracks())[0]
        self.assertIsInstance(track, deezer.resources.Track)

    def test_artist_attributes(self):
        """
        Test artist resource
        """
        client = deezer.Client()
        artist = client.get_artist(27)
        self.assertTrue(hasattr(artist, 'name'))
        self.assertIsInstance(artist, deezer.resources.Artist)
        self.assertEqual(repr(artist), '<Artist: Daft Punk>')

    def test_artist_albums(self):
        """
        Test albums method of artist resource
        """
        client = deezer.Client()
        artist = client.get_artist(27)
        albums = artist.get_albums()
        self.assertIsInstance(albums, list)
        album = albums[0]
        self.assertIsInstance(album, deezer.resources.Album)
        self.assertEqual(repr(album),
                         '<Album: Human After All (Remixes) (Remixes)>')
        self.assertEqual(type(artist.iter_albums()), GeneratorType)

    def test_artist_top(self):
        """
        Test top method of artist resource
        """
        client = deezer.Client()
        artist = client.get_artist(27)
        tracks = artist.get_top()
        self.assertIsInstance(tracks, list)
        track = tracks[0]
        self.assertIsInstance(track, deezer.resources.Track)
        self.assertEqual(repr(track), '<Track: Get Lucky (Radio Edit)>')

    def test_artist_radio(self):
        """
        Test radio method of artist resource
        """
        client = deezer.Client()
        artist = client.get_artist(27)
        tracks = artist.get_radio()
        self.assertIsInstance(tracks, list)
        track = tracks[0]
        self.assertIsInstance(track, deezer.resources.Track)
        self.assertEqual(repr(track), '<Track: Lose Yourself to Dance>')

    def test_artist_related(self):
        """
        Test related method of artist resource
        """
        client = deezer.Client()
        artist = client.get_artist(27)
        artists = artist.get_related()
        self.assertIsInstance(artists, list)
        artist = artists[0]
        self.assertIsInstance(artist, deezer.resources.Artist)
        self.assertEqual(repr(artist), '<Artist: Justice>')
        self.assertEqual(type(artist.iter_related()), GeneratorType)

    def test_track_attributes(self):
        """
        Test track resource
        """
        client = deezer.Client()
        track = client.get_track(3135556)
        artist = track.get_artist()
        album = track.get_album()
        self.assertTrue(hasattr(track, 'title'))
        self.assertIsInstance(track, deezer.resources.Track)
        self.assertIsInstance(artist, deezer.resources.Artist)
        self.assertIsInstance(album, deezer.resources.Album)
        self.assertEqual(repr(track), '<Track: Harder Better Faster Stronger>')
        self.assertEqual(repr(artist), '<Artist: Daft Punk>')
        self.assertEqual(repr(album), '<Album: Discovery>')

    def test_radio_attributes(self):
        """
        Test radio resource
        """
        client = deezer.Client()
        radio = client.get_radio(23261)
        self.assertTrue(hasattr(radio, 'title'))
        self.assertIsInstance(radio, deezer.resources.Radio)
        self.assertEqual(repr(radio), '<Radio: Telegraph Classical>')

    def test_radio_tracks(self):
        """
        Test tracks method of radio resource
        """
        client = deezer.Client()
        radio = client.get_radio(23261)
        tracks = radio.get_tracks()
        self.assertIsInstance(tracks, list)
        track = tracks[2]
        self.assertIsInstance(track, deezer.resources.Track)
        self.assertEqual(type(radio.iter_tracks()), GeneratorType)

    def test_genre_attributes(self):
        """
        Test genre resource
        """
        client = deezer.Client()
        genre = client.get_genre(106)
        self.assertTrue(hasattr(genre, 'name'))
        self.assertIsInstance(genre, deezer.resources.Genre)
        self.assertEqual(repr(genre), '<Genre: Electro>')

    def test_genre_artists(self):
        """
        Test artists method of genre resource
        """
        client = deezer.Client()
        genre = client.get_genre(106)
        artists = genre.get_artists()
        self.assertIsInstance(artists, list)
        artist = artists[0]
        self.assertIsInstance(artist, deezer.resources.Artist)
        self.assertEqual(repr(artist), '<Artist: Calvin Harris>')
        self.assertEqual(type(genre.iter_artists()), GeneratorType)

    def test_genre_radios(self):
        """
        Test radios method of genre resource
        """
        client = deezer.Client()
        genre = client.get_genre(106)
        radios = genre.get_radios()
        self.assertIsInstance(radios, list)
        radio = radios[0]
        self.assertIsInstance(radio, deezer.resources.Radio)
        self.assertEqual(repr(radio), '<Radio: Techno/House>')
        self.assertEqual(type(genre.iter_radios()), GeneratorType)

    def test_chart_tracks(self):
        """
        Test tracks method of chart resource
        """
        client = deezer.Client()
        chart = client.get_chart()
        tracks = chart.get_tracks()
        self.assertIsInstance(tracks, list)
        track = tracks[0]
        self.assertIsInstance(track, deezer.resources.Track)
        self.assertEqual(repr(track), '<Track: Starboy>')
        self.assertEqual(type(chart.iter_tracks()), GeneratorType)

    def test_chart_artists(self):
        """
        Test artists method of chart resource
        """
        client = deezer.Client()
        chart = client.get_chart()
        artists = chart.get_artists()
        self.assertIsInstance(artists, list)
        artist = artists[0]
        self.assertIsInstance(artist, deezer.resources.Artist)
        self.assertEqual(repr(artist), '<Artist: Pnl>')
        self.assertEqual(type(chart.iter_artists()), GeneratorType)

    def test_chart_albums(self):
        """
        Test albums method of chart resource
        """
        client = deezer.Client()
        chart = client.get_chart()
        albums = chart.get_albums()
        self.assertIsInstance(albums, list)
        album = albums[0]
        self.assertIsInstance(album, deezer.resources.Album)
        self.assertEqual(repr(album),
                         "<Album: Where Is l'album de Gradur>")
        self.assertEqual(type(chart.iter_albums()), GeneratorType)

    def test_chart_playlists(self):
        """
        Test playlists method of chart resource
        """
        client = deezer.Client()
        chart = client.get_chart()
        playlists = chart.get_playlists()
        self.assertIsInstance(playlists, list)
        playlist = playlists[0]
        self.assertIsInstance(playlist, deezer.resources.Playlist)
        self.assertEqual(repr(playlist),
                         "<Playlist: Top France>")
        self.assertEqual(type(chart.iter_playlists()), GeneratorType)
