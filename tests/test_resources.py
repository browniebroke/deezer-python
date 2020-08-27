from types import GeneratorType

import pytest

import deezer

pytestmark = pytest.mark.vcr


class TestResource:
    def test_resource_relation(self, client):
        """Test passing parent object when using get_relation."""
        album = client.get_album(302127)
        tracks = album.get_tracks()
        assert tracks[0].album is album


class TestAlbum:
    def test_album_attributes(self, client):
        """
        Test album resource
        """
        album = client.get_album(302127)
        assert hasattr(album, "title")
        assert repr(album) == "<Album: Discovery>"

        artist = album.get_artist()
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Daft Punk>"

    def test_album_tracks(self, client):
        """
        Test tracks method of album resource
        """
        album = client.get_album(302127)

        # tests list
        tracks = album.get_tracks()
        assert isinstance(tracks, list)
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: One More Time>"

        # tests generator
        tracks_generator = album.iter_tracks()
        assert type(tracks_generator) == GeneratorType
        track = next(tracks_generator)
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: One More Time>"

    def test_as_dict(self, client):
        """
        Test resource conversion to dict
        """
        album = client.get_album(302127)
        assert album.asdict()["id"] == 302127


class TestArtist:
    def test_artist_attributes(self, client):
        """
        Test artist resource
        """
        artist = client.get_artist(27)
        assert hasattr(artist, "name")
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Daft Punk>"

    def test_artist_albums(self, client):
        """
        Test albums method of artist resource
        """
        artist = client.get_artist(27)

        # tests list
        albums = artist.get_albums()
        assert isinstance(albums, list)
        album = albums[0]
        assert isinstance(album, deezer.resources.Album)
        assert repr(album) == "<Album: Random Access Memories>"

        # tests generator
        albums_generator = artist.iter_albums()
        assert type(albums_generator) == GeneratorType
        album = next(albums_generator)
        assert isinstance(album, deezer.resources.Album)
        assert repr(album) == "<Album: Random Access Memories>"

    def test_artist_top(self, client):
        """
        Test top method of artist resource
        """
        artist = client.get_artist(27)
        tracks = artist.get_top()
        assert isinstance(tracks, list)
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: Instant Crush>"

    def test_artist_radio(self, client):
        """
        Test radio method of artist resource
        """
        artist = client.get_artist(27)
        tracks = artist.get_radio()
        assert isinstance(tracks, list)
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: One More Time>"

    def test_artist_related(self, client):
        """
        Test related method of artist resource
        """
        artist = client.get_artist(27)

        # tests list
        related_artists = artist.get_related()
        assert isinstance(related_artists, list)
        related_artist = related_artists[0]
        assert isinstance(related_artist, deezer.resources.Artist)
        assert repr(related_artist) == "<Artist: Justice>"

        # tests generator
        related_artists_generator = artist.iter_related()
        assert type(related_artists_generator) == GeneratorType
        related_artist = next(related_artists_generator)
        assert isinstance(related_artist, deezer.resources.Artist)
        assert repr(related_artist) == "<Artist: Justice>"


class TestTrack:
    def test_track_attributes(self, client):
        """
        Test track resource
        """
        track = client.get_track(3135556)
        artist = track.get_artist()
        album = track.get_album()
        assert hasattr(track, "title")
        assert isinstance(track, deezer.resources.Track)
        assert isinstance(artist, deezer.resources.Artist)
        assert isinstance(album, deezer.resources.Album)
        assert repr(track) == "<Track: Harder Better Faster Stronger>"
        assert repr(artist) == "<Artist: Daft Punk>"
        assert repr(album) == "<Album: Discovery>"


class TestRadio:
    def test_radio_attributes(self, client):
        """
        Test radio resource
        """
        radio = client.get_radio(23261)
        assert hasattr(radio, "title")
        assert isinstance(radio, deezer.resources.Radio)
        assert repr(radio) == "<Radio: Telegraph Classical>"

    def test_radio_tracks(self, client):
        """
        Test tracks method of radio resource
        """
        radio = client.get_radio(23261)

        # tests list
        tracks = radio.get_tracks()
        assert isinstance(tracks, list)
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert (
            repr(track)
            == '<Track: Mozart: Piano Concerto No. 9 in E-Flat Major, K. 271 "Jeunehomme": I. Allegro>'
        )

        # tests generator
        tracks_generator = radio.iter_tracks()
        assert type(tracks_generator) == GeneratorType
        track = next(tracks_generator)
        assert isinstance(track, deezer.resources.Track)
        assert (
            repr(track)
            == '<Track: Mozart: Piano Concerto No. 9 in E-Flat Major, K. 271 "Jeunehomme": I. Allegro>'
        )


class TestGenre:
    def test_genre_attributes(self, client):
        """
        Test genre resource
        """
        genre = client.get_genre(106)
        assert hasattr(genre, "name")
        assert isinstance(genre, deezer.resources.Genre)
        assert repr(genre) == "<Genre: Electro>"

    def test_genre_artists(self, client):
        """
        Test artists method of genre resource
        """
        genre = client.get_genre(106)

        # tests list
        artists = genre.get_artists()
        assert isinstance(artists, list)
        artist = artists[0]
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Major Lazer>"

        # tests generator
        artists_generator = genre.iter_artists()
        assert type(artists_generator) == GeneratorType
        artist = next(artists_generator)
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Major Lazer>"

    def test_genre_radios(self, client):
        """
        Test radios method of genre resource
        """
        genre = client.get_genre(106)

        # tests list
        radios = genre.get_radios()
        assert isinstance(radios, list)
        radio = radios[0]
        assert isinstance(radio, deezer.resources.Radio)
        assert repr(radio) == "<Radio: Electro Swing>"
        assert type(genre.iter_radios()) == GeneratorType

        # tests generator
        radios_generator = genre.iter_radios()
        assert type(radios_generator) == GeneratorType
        radio = next(radios_generator)
        assert isinstance(radio, deezer.resources.Radio)
        assert repr(radio) == "<Radio: Electro Swing>"


class TestChart:
    def test_chart_tracks(self, client):
        """
        Test tracks method of chart resource
        """
        chart = client.get_chart()

        # tests list
        tracks = chart.get_tracks()
        assert isinstance(tracks, list)
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: Head & Heart (feat. MNEK)>"

        # tests generator
        tracks_generator = chart.iter_tracks()
        assert type(tracks_generator) == GeneratorType
        track = next(tracks_generator)
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: Head & Heart (feat. MNEK)>"

    def test_chart_artists(self, client):
        """
        Test artists method of chart resource
        """
        chart = client.get_chart()

        # tests list
        artists = chart.get_artists()
        assert isinstance(artists, list)
        artist = artists[0]
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Juice Wrld>"
        assert type(chart.iter_artists()) == GeneratorType

        # tests generator
        artists_generator = chart.iter_artists()
        assert type(artists_generator) == GeneratorType
        artist = next(artists_generator)
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Juice Wrld>"

    def test_chart_albums(self, client):
        """
        Test albums method of chart resource
        """
        chart = client.get_chart()

        # tests list
        albums = chart.get_albums()
        assert isinstance(albums, list)
        album = albums[0]
        assert isinstance(album, deezer.resources.Album)
        assert repr(album) == "<Album: folklore>"

        # tests generator
        albums_generator = chart.iter_albums()
        assert type(albums_generator) == GeneratorType
        album = next(albums_generator)
        assert isinstance(album, deezer.resources.Album)
        assert repr(album) == "<Album: folklore>"

    def test_chart_playlists(self, client):
        """
        Test playlists method of chart resource
        """
        chart = client.get_chart()

        # tests list
        playlists = chart.get_playlists()
        assert isinstance(playlists, list)
        playlist = playlists[0]
        assert isinstance(playlist, deezer.resources.Playlist)
        assert repr(playlist) == "<Playlist: Deezer Hits UK>"

        # tests generator
        playlists_generator = chart.iter_playlists()
        assert type(playlists_generator) == GeneratorType
        playlist = next(playlists_generator)
        assert isinstance(playlist, deezer.resources.Playlist)
        assert repr(playlist) == "<Playlist: Deezer Hits UK>"


class TestUser:
    def test_user_albums(self, client):
        """
        Test albums method of user resource
        """
        user = client.get_user(359622)

        # tests list
        albums = user.get_albums()
        assert isinstance(albums, list)
        album = albums[0]
        assert isinstance(album, deezer.resources.Album)
        assert repr(album) == "<Album: A Century Of Movie Soundtracks Vol. 2>"

        # tests generator
        albums_generator = user.iter_albums()
        assert type(albums_generator) == GeneratorType
        album = next(albums_generator)
        assert isinstance(album, deezer.resources.Album)
        assert repr(album) == "<Album: A Century Of Movie Soundtracks Vol. 2>"

    def test_user_artists(self, client):
        """
        Test artists method of user resource
        """
        user = client.get_user(359622)

        # tests list
        artists = user.get_artists()
        assert isinstance(artists, list)
        artist = artists[0]
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Wax Tailor>"

        # tests generator
        artists_generator = user.iter_artists()
        assert type(artists_generator) == GeneratorType
        artist = next(artists_generator)
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Wax Tailor>"

    def test_user_playlists(self, client):
        """
        Test playlists method of user resource
        """
        user = client.get_user(359622)

        # tests list
        playlists = user.get_playlists()
        assert isinstance(playlists, list)
        playlist = playlists[0]
        assert isinstance(playlist, deezer.resources.Playlist)
        assert repr(playlist) == "<Playlist: AC/DC>"

        # tests generator
        playlists_generator = user.iter_playlists()
        assert type(playlists_generator) == GeneratorType
        playlist = next(playlists_generator)
        assert isinstance(playlist, deezer.resources.Playlist)
        assert repr(playlist) == "<Playlist: AC/DC>"

    def test_user_tracks(self, client):
        """
        Test tracks method of user resource
        """
        user = client.get_user(353978015)

        # tests list
        tracks = user.get_tracks()
        assert isinstance(tracks, list)
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: Prélude a l'après-midi d'un faune, L. 86>"

        # tests generator
        tracks_generator = user.iter_tracks()
        assert type(tracks_generator) == GeneratorType
        track = next(tracks_generator)
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: Prélude a l'après-midi d'un faune, L. 86>"


class TestPlaylist:
    def test_get_tracks(self, client):
        """
        Test tracks method of playlist resource
        """
        playlist = client.get_playlist(12345)

        # tests list
        tracks = playlist.get_tracks()
        assert isinstance(tracks, list)
        assert len(tracks) == 4
        assert all(isinstance(track, deezer.resources.Track) for track in tracks)
        assert tracks[0].title == "Skanky Panky"

        # tests generator
        tracks_generator = playlist.iter_tracks()
        assert type(tracks_generator) == GeneratorType
        playlist_tracks = list(tracks_generator)
        # this is weird (the length being different), it seems there's a sort of
        # partially-hidden track that only shows up when using the method in
        # iter_tracks
        assert len(playlist_tracks) == 5
        assert all(
            isinstance(track, deezer.resources.Track) for track in playlist_tracks
        )
        assert playlist_tracks[0].title == "Skanky Panky"

    def test_get_fans(self, client):
        """
        Test fans method of playlist resource
        """
        playlist = client.get_playlist(6512)

        # tests list
        fans = playlist.get_fans()
        assert isinstance(fans, list)
        assert len(fans) == 3
        for fan in fans:
            assert isinstance(fan, deezer.resources.User)
        assert fans[0].name == "laurentky"

        # tests generator
        fans_generator = playlist.iter_fans()
        assert type(fans_generator) == GeneratorType
        fan = next(fans_generator)
        assert fan.name == "laurentky"
        count = 1
        while 1:
            assert isinstance(fan, deezer.resources.User)
            try:
                fan = next(fans_generator)
                count += 1
            except StopIteration:
                break
        assert count == 3


class TestPodcast:
    def test_get_episodes(self, client):
        """
        Test episodes method of podcast resource
        """
        podcast = client.get_podcast(699612)

        # tests list
        episodes = podcast.get_episodes()
        assert isinstance(episodes, list)
        assert len(episodes) == 12
        for episode in episodes:
            assert isinstance(episode, deezer.resources.Episode)
        assert episodes[0].title == "Episode 9: Follow the money"

        # tests generator
        episodes_generator = podcast.iter_episodes()
        assert type(episodes_generator) == GeneratorType
        episode = next(episodes_generator)
        assert episode.title == "Episode 9: Follow the money"
        count = 1
        while 1:
            assert isinstance(episode, deezer.resources.Episode)
            try:
                episode = next(episodes_generator)
                count += 1
            except StopIteration:
                break
        assert count == 12
