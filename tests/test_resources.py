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

    def test_contributors(self, client):
        album = client.get_album(302128)

        contributors = album.contributors
        assert isinstance(contributors, list)
        assert len(contributors) == 2
        assert all(isinstance(c, deezer.resources.Artist) for c in contributors)
        assert [c.id for c in contributors] == [123021, 6159602]

    def test_as_dict(self, client):
        """
        Test resource conversion to dict
        """
        album = client.get_album(302127)
        album_dict = album.as_dict()
        assert album_dict["id"] == 302127
        assert album_dict["release_date"] == "2001-03-07"

    def test_rate(self, client_token):
        album = deezer.resources.Album(client_token, {"id": 302127})
        result = album.rate(3)
        assert result is True


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

    def test_contributors(self, client):
        track = client.get_track(1425844092)
        contributors = track.contributors
        assert isinstance(contributors, list)
        assert len(contributors) == 2
        assert all(isinstance(c, deezer.resources.Artist) for c in contributors)
        assert [c.id for c in contributors] == [51204222, 288166]


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
    @pytest.fixture()
    def chart(self, client):
        return deezer.resources.Chart(client, {})

    def test_get_tracks(self, chart):
        tracks = chart.get_tracks()
        assert isinstance(tracks, list)
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: Bad Habits>"

    def test_iter_tracks(self, chart):
        tracks_generator = chart.iter_tracks()
        assert type(tracks_generator) == GeneratorType
        track = next(tracks_generator)
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: Bad Habits>"

    def test_get_artists(self, chart):
        artists = chart.get_artists()
        assert isinstance(artists, list)
        artist = artists[0]
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Kanye West>"

    def test_iter_artists(self, chart):
        artists_generator = chart.iter_artists()
        assert type(artists_generator) == GeneratorType
        artist = next(artists_generator)
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Kanye West>"

    def test_get_albums(self, chart):
        albums = chart.get_albums()
        assert isinstance(albums, list)
        album = albums[0]
        assert isinstance(album, deezer.resources.Album)
        assert repr(album) == "<Album: Music Of The Spheres>"

    def test_iter_albums(self, chart):
        albums_generator = chart.iter_albums()
        assert type(albums_generator) == GeneratorType
        album = next(albums_generator)
        assert isinstance(album, deezer.resources.Album)
        assert repr(album) == "<Album: Music Of The Spheres>"

    def test_get_playlists(self, chart):
        playlists = chart.get_playlists()
        assert isinstance(playlists, list)
        playlist = playlists[0]
        assert isinstance(playlist, deezer.resources.Playlist)
        assert repr(playlist) == "<Playlist: Brand New UK>"

    def test_iter_playlists(self, chart):
        playlists_generator = chart.iter_playlists()
        assert type(playlists_generator) == GeneratorType
        playlist = next(playlists_generator)
        assert isinstance(playlist, deezer.resources.Playlist)
        assert repr(playlist) == "<Playlist: Brand New UK>"


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


class TestEpisode:
    def test_get_episode(self, client):
        episode = client.get_episode(343457312)
        assert isinstance(episode, deezer.resources.Episode)
        assert episode.title == "Stuart Hogg and the GOAT"

    def test_as_dict(self, client):
        """Test resource conversion to dict."""
        episode = client.get_episode(343457312)
        episode_dict = episode.as_dict()
        assert episode_dict["id"] == 343457312
        assert episode_dict["release_date"] == "2021-11-22 23:42:00"
