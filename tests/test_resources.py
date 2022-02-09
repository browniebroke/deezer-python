from __future__ import annotations

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
    def test_basic(self, client):
        """Test basic Album resource."""
        album = client.get_album(302127)
        assert hasattr(album, "title")
        assert repr(album) == "<Album: Discovery>"

        artist = album.get_artist()
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Daft Punk>"

    def test_get_tracks(self, client):
        album = client.get_album(302127)

        # tests pagination
        tracks = album.get_tracks()
        assert isinstance(tracks, deezer.pagination.PaginatedList)
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: One More Time>"
        assert len(tracks) == 14

    def test_contributors(self, client):
        album = client.get_album(302128)

        contributors = album.contributors
        assert isinstance(contributors, list)
        assert len(contributors) == 2
        assert all(isinstance(c, deezer.resources.Artist) for c in contributors)
        assert [c.id for c in contributors] == [123021, 6159602]

    def test_as_dict(self, client):
        album = client.get_album(302127)
        album_dict = album.as_dict()
        assert album_dict["id"] == 302127
        assert album_dict["release_date"] == "2001-03-07"

    def test_rate(self, client_token):
        album = deezer.resources.Album(client_token, {"id": 302127})
        result = album.rate(3)
        assert result is True


class TestArtist:
    @pytest.fixture()
    def daft_punk(self, client):
        return client.get_artist(27)

    def test_attributes(self, daft_punk):
        assert hasattr(daft_punk, "name")
        assert isinstance(daft_punk, deezer.resources.Artist)
        assert repr(daft_punk) == "<Artist: Daft Punk>"

    def test_get_albums(self, daft_punk):
        albums = daft_punk.get_albums()
        assert isinstance(albums, deezer.pagination.PaginatedList)
        album = albums[0]
        assert isinstance(album, deezer.resources.Album)
        assert repr(album) == "<Album: Random Access Memories>"
        assert len(albums) == 32

    def test_get_top(self, daft_punk):
        tracks = daft_punk.get_top()
        assert isinstance(tracks, deezer.pagination.PaginatedList)
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: Instant Crush>"
        assert len(tracks) == 100

    def test_get_radio(self, daft_punk):
        tracks = daft_punk.get_radio()
        assert isinstance(tracks, list)
        assert len(tracks) == 25
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: One More Time>"

    def test_get_related(self, daft_punk):
        related_artists = daft_punk.get_related()
        assert isinstance(related_artists, deezer.pagination.PaginatedList)
        related_artist = related_artists[0]
        assert isinstance(related_artist, deezer.resources.Artist)
        assert repr(related_artist) == "<Artist: Justice>"
        assert len(related_artists) == 39

    def test_get_playlists(self, daft_punk):
        playlists = daft_punk.get_playlists()
        assert isinstance(playlists, deezer.pagination.PaginatedList)
        playlist = playlists[0]
        assert isinstance(playlist, deezer.resources.Playlist)
        assert repr(playlist) == "<Playlist: En mode 90>"
        assert len(playlists) == 100


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
    @pytest.fixture
    def radio(self, client):
        return client.get_radio(23261)

    def test_attributes(self, radio):
        assert hasattr(radio, "title")
        assert isinstance(radio, deezer.resources.Radio)
        assert repr(radio) == "<Radio: Telegraph Classical>"

    def test_get_tracks(self, radio):
        tracks = radio.get_tracks()
        assert isinstance(tracks, list)
        assert len(tracks) == 25
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert (
            repr(track)
            == '<Track: Mozart: Piano Concerto No. 9 in E-Flat Major, K. 271 "Jeunehomme": I. Allegro>'
        )


class TestGenre:
    @pytest.fixture
    def electro(self, client):
        return client.get_genre(106)

    def test_attributes(self, electro):
        assert hasattr(electro, "name")
        assert isinstance(electro, deezer.resources.Genre)
        assert repr(electro) == "<Genre: Electro>"

    def test_get_artists(self, electro):
        artists = electro.get_artists()
        assert isinstance(artists, list)
        assert len(artists) == 48
        artist = artists[0]
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Major Lazer>"

    def test_get_podcasts(self, client):
        technology = client.get_genre(232)
        podcasts = technology.get_podcasts()
        assert isinstance(podcasts, deezer.pagination.PaginatedList)
        podcast = podcasts[0]
        assert isinstance(podcast, deezer.resources.Podcast)
        assert repr(podcast) == "<Podcast: Le rendez-vous Tech>"
        assert len(podcasts) == 15

    def test_get_radios(self, electro):
        radios = electro.get_radios()
        assert isinstance(radios, list)
        assert len(radios) == 32
        radio = radios[0]
        assert isinstance(radio, deezer.resources.Radio)
        assert repr(radio) == "<Radio: Electro Swing>"


class TestChart:
    @pytest.fixture()
    def chart(self, client):
        return deezer.resources.Chart(client, {})

    def test_get_tracks(self, chart):
        tracks = chart.get_tracks()
        assert isinstance(tracks, deezer.pagination.PaginatedList)
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: Bad Habits>"
        assert len(tracks) == 10

    def test_get_artists(self, chart):
        artists = chart.get_artists()
        assert isinstance(artists, deezer.pagination.PaginatedList)
        artist = artists[0]
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Kanye West>"
        assert len(artists) == 10

    def test_get_albums(self, chart):
        albums = chart.get_albums()
        assert isinstance(albums, deezer.pagination.PaginatedList)
        album = albums[0]
        assert isinstance(album, deezer.resources.Album)
        assert repr(album) == "<Album: Music Of The Spheres>"
        assert len(albums) == 10

    def test_get_playlists(self, chart):
        playlists = chart.get_playlists()
        assert isinstance(playlists, deezer.pagination.PaginatedList)
        playlist = playlists[0]
        assert isinstance(playlist, deezer.resources.Playlist)
        assert repr(playlist) == "<Playlist: Brand New UK>"
        assert len(playlists) == 10


class TestUser:
    @pytest.fixture
    def user(self, client):
        return client.get_user(359622)

    def test_get_albums(self, user):
        albums = user.get_albums()
        assert isinstance(albums, deezer.resources.PaginatedList)
        album = albums[0]
        assert isinstance(album, deezer.resources.Album)
        assert repr(album) == "<Album: A Century Of Movie Soundtracks Vol. 2>"
        assert len(albums) == 7

    def test_get_artists(self, user):
        artists = user.get_artists()
        assert isinstance(artists, deezer.pagination.PaginatedList)
        artist = artists[0]
        assert isinstance(artist, deezer.resources.Artist)
        assert repr(artist) == "<Artist: Wax Tailor>"
        assert len(artists) == 7

    def test_get_playlists(self, user):
        playlists = user.get_playlists()
        assert isinstance(playlists, deezer.pagination.PaginatedList)
        playlist = playlists[0]
        assert isinstance(playlist, deezer.resources.Playlist)
        assert repr(playlist) == "<Playlist: AC/DC>"
        assert len(playlists) == 25

    def test_get_tracks(self, user):
        tracks = user.get_tracks()
        assert isinstance(tracks, deezer.pagination.PaginatedList)
        track = tracks[0]
        assert isinstance(track, deezer.resources.Track)
        assert repr(track) == "<Track: Poney Pt. I>"
        assert len(tracks) == 3


class TestPlaylist:
    @pytest.fixture
    def playlist(self, client):
        return client.get_playlist(9200461)

    def test_attributes(self, playlist):
        assert playlist.title == "Lounge Soirée"

    def test_get_tracks(self, playlist):
        tracks = playlist.get_tracks()
        assert isinstance(tracks, deezer.pagination.PaginatedList)
        first_track = tracks[0]
        assert isinstance(first_track, deezer.resources.Track)
        assert first_track.title == "Otherwise"
        assert len(tracks) == 102

    def test_get_fans(self, playlist):
        fans = playlist.get_fans()
        assert isinstance(fans, deezer.pagination.PaginatedList)
        first_fan = fans[0]
        assert isinstance(first_fan, deezer.resources.User)
        assert first_fan.name == "Fay22"
        assert len(fans) == 100


class TestPodcast:
    def test_get_episodes(self, client):
        podcast = client.get_podcast(699612)

        episodes = podcast.get_episodes()
        assert isinstance(episodes, deezer.pagination.PaginatedList)
        episode = episodes[0]
        assert isinstance(episode, deezer.resources.Episode)
        assert episode.title == "Episode 9: Follow the money"
        assert len(episodes) == 12


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


class TestEditorial:
    @pytest.fixture
    def editorial(self, client):
        return client.get_editorial(106)

    def test_attributes(self, editorial):
        assert hasattr(editorial, "name")
        assert isinstance(editorial, deezer.resources.Editorial)
        assert repr(editorial) == "<Editorial: Electro>"

    def test_get_selection(self, editorial):
        albums = editorial.get_selection()
        assert isinstance(albums, list)
        assert len(albums) == 10
        album = albums[0]
        assert isinstance(album, deezer.resources.Album)
        assert album.title == "Terre Promise"

    def test_get_chart(self, editorial):
        charts = editorial.get_chart()
        assert isinstance(charts, deezer.resources.Chart)

        assert isinstance(charts.tracks[0], deezer.resources.Track)
        assert isinstance(charts.albums[0], deezer.resources.Album)
        assert isinstance(charts.artists[0], deezer.resources.Artist)
        assert isinstance(charts.playlists[0], deezer.resources.Playlist)

    def test_get_releases(self, editorial):
        albums = editorial.get_releases()
        assert isinstance(albums, deezer.pagination.PaginatedList)
        album = albums[0]
        assert isinstance(album, deezer.resources.Album)
        assert repr(album) == "<Album: Girls>"
        assert len(albums) == 199
