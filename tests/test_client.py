import pytest
import requests

import deezer
from deezer.exceptions import (
    DeezerErrorResponse,
    DeezerNotFoundError,
    DeezerUnknownResource,
)

pytestmark = pytest.mark.vcr


class TestClient:
    def test_access_token_set(self, client, mocker):
        """Test that access token is set when making the request."""
        session_get = mocker.patch.object(requests.Session, "request")
        client.access_token = "token"
        assert client.access_token, "token"
        client.request("GET", "user/me")
        session_get.assert_called_with(
            "GET",
            "https://api.deezer.com/user/me",
            params={"access_token": "token"},
        )

    def test_request_404(self, client):
        with pytest.raises(DeezerNotFoundError):
            client.request("GET", "does-not-exists")

    def test_request_unknown_resource(self, client):
        with pytest.raises(DeezerUnknownResource):
            client.request("GET", "chart")

    def test_get_album(self, client):
        """Test method to retrieve an album"""
        album = client.get_album(302127)
        assert isinstance(album, deezer.resources.Album)

    def test_no_album_raise(self, client):
        """Test method get_album for invalid value"""
        with pytest.raises(DeezerErrorResponse):
            client.get_album(-1)

    def test_get_artist(self, client):
        """Test methods to get an artist"""
        artist = client.get_artist(27)
        assert isinstance(artist, deezer.resources.Artist)

    def test_chart(self, client):
        result = client.get_chart()
        assert isinstance(result, deezer.resources.Chart)

        assert isinstance(result.tracks[0], deezer.resources.Track)
        assert isinstance(result.albums[0], deezer.resources.Album)
        assert isinstance(result.artists[0], deezer.resources.Artist)
        assert isinstance(result.playlists[0], deezer.resources.Playlist)

    def test_tracks_chart(self, client):
        result = client.get_tracks_chart()
        assert isinstance(result, list)
        assert result[0].title == "Khapta"
        assert isinstance(result[0], deezer.resources.Track)

    def test_albums_chart(self, client):
        result = client.get_albums_chart()
        assert isinstance(result, list)
        assert result[0].title == "Lacrim"
        assert isinstance(result[0], deezer.resources.Album)

    def test_artists_chart(self, client):
        result = client.get_artists_chart()
        assert isinstance(result, list)
        assert result[0].name == "Lacrim"
        assert isinstance(result[0], deezer.resources.Artist)

    def test_playlists_chart(self, client):
        result = client.get_playlists_chart()
        assert isinstance(result, list)
        assert result[0].title == "Les titres du moment"
        assert isinstance(result[0], deezer.resources.Playlist)

    def test_podcasts_chart(self, client):
        result = client.get_podcasts_chart()
        assert isinstance(result, list)
        assert result[0].title == "Rob Beckett and Josh Widdicombe's Parenting Hell"
        assert isinstance(result[0], deezer.resources.Podcast)

    def test_get_episode(self, client):
        """Test methods to get an episode"""
        episode = client.get_episode(238455362)
        assert isinstance(episode, deezer.resources.Episode)

    def test_no_episode_raise(self, client):
        """Test method get_episode for invalid value"""
        with pytest.raises(DeezerErrorResponse):
            client.get_episode(-1)

    def test_get_genre(self, client):
        """Test methods to get a genre"""
        genre = client.get_genre(106)
        assert isinstance(genre, deezer.resources.Genre)

    def test_no_genre_raise(self, client):
        """Test method get_genre for invalid value"""
        with pytest.raises(DeezerErrorResponse):
            client.get_genre(-1)

    def test_list_genres(self, client):
        """Test methods to list several genres"""
        genres = client.list_genres()
        assert isinstance(genres, list)
        assert isinstance(genres[0], deezer.resources.Genre)

    def test_get_playlist(self, client):
        """Test methods to get a playlist"""
        playlist = client.get_playlist(908622995)
        assert isinstance(playlist, deezer.resources.Playlist)

    def test_no_playlist_raise(self, client):
        """Test method get_playlist for invalid value"""
        with pytest.raises(DeezerErrorResponse):
            client.get_playlist(-1)

    def test_get_podcast(self, client):
        """Test methods to get a podcast"""
        podcast = client.get_podcast(699612)
        assert isinstance(podcast, deezer.resources.Podcast)

    def test_no_podcast_raise(self, client):
        """Test method get_podcast for invalid value"""
        with pytest.raises(DeezerErrorResponse):
            client.get_podcast(-1)

    def test_get_radio(self, client):
        """Test methods to get a radio"""
        radio = client.get_radio(23261)
        assert isinstance(radio, deezer.resources.Radio)

    def test_no_radio_raise(self, client):
        """Test method get_radio for invalid value"""
        with pytest.raises(DeezerErrorResponse):
            client.get_radio(-1)

    def test_list_radios(self, client):
        """Test methods to list radios"""
        radios = client.list_radios()
        assert isinstance(radios, list)
        assert isinstance(radios[0], deezer.resources.Radio)

    def test_get_radios_top(self, client):
        radios = client.get_radios_top()
        assert isinstance(radios, list)
        assert isinstance(radios[0], deezer.resources.Radio)

    def test_get_track(self, client):
        """Test methods to get a track"""
        track = client.get_track(3135556)
        assert isinstance(track, deezer.resources.Track)

    def test_no_track_raise(self, client):
        """Test method get_track for invalid value"""
        with pytest.raises(DeezerErrorResponse):
            client.get_track(-1)

    def test_get_user(self, client):
        """Test methods to get a user"""
        user = client.get_user(359622)
        assert isinstance(user, deezer.resources.User)

    def test_get_current_user(self, client_token):
        """Test methods to get the current user"""
        user = client_token.get_user()
        assert isinstance(user, deezer.resources.User)

    def test_no_user_raise(self, client):
        """Test method get_user for invalid value"""
        with pytest.raises(DeezerErrorResponse):
            client.get_user(-1)

    @pytest.mark.parametrize(
        "args",
        [
            (),
            (359622,),
        ],
    )
    def test_get_user_albums(self, client_token, args):
        user_albums = client_token.get_user_albums(*args)
        assert len(user_albums) == 2
        assert all(isinstance(a, deezer.resources.Album) for a in user_albums)
        assert user_albums[0].title == "OK Cowboy"
        assert user_albums[1].title == "Tank (Remastered)"

    def test_add_user_album(self, client_token):
        result = client_token.add_user_album(302127)
        assert result is True

    def test_remove_user_album(self, client_token):
        result = client_token.remove_user_album(302127)
        assert result is True

    @pytest.mark.parametrize(
        "args",
        [
            (),
            (359622,),
        ],
    )
    def test_get_user_artists(self, client_token, args):
        user_artists = client_token.get_user_artists(*args)
        assert len(user_artists) == 4
        assert all(isinstance(a, deezer.resources.Artist) for a in user_artists)
        assert [a.name for a in user_artists] == [
            "Wax Tailor",
            "Vitalic",
            "Morcheeba",
            "Tribute Stars",
        ]

    def test_add_user_artist(self, client_token):
        result = client_token.add_user_artist(243)
        assert result is True

    def test_remove_user_artist(self, client_token):
        result = client_token.remove_user_artist(243)
        assert result is True

    def test_get_user_history(self, client_token):
        user_history = client_token.get_user_history()
        assert len(user_history) == 3
        assert all(isinstance(t, deezer.resources.Track) for t in user_history)
        assert [t.title for t in user_history] == [
            "Loverini",
            "Superchérie",
            "Run Away",
        ]

    @pytest.mark.parametrize(
        "args",
        [
            (),
            (359622,),
        ],
    )
    def test_get_user_tracks(self, client_token, args):
        user_tracks = client_token.get_user_tracks(*args)
        assert len(user_tracks) == 3
        assert all(isinstance(a, deezer.resources.Track) for a in user_tracks)
        assert [t.title for t in user_tracks] == [
            "Flyover",
            "Poney Pt. I",
            "Young Blood",
        ]

    def test_add_user_track(self, client_token):
        result = client_token.add_user_track(1374789602)
        assert result is True

    def test_remove_user_track(self, client_token):
        result = client_token.remove_user_track(1374789602)
        assert result is True

    def test_search_simple(self, client):
        """Test search method"""
        result = client.search("Soliloquy")
        assert isinstance(result, list)
        assert all(isinstance(r, deezer.resources.Track) for r in result)
        assert result[0].title == "Soliloquy"

    @pytest.mark.parametrize(
        ("params", "expected_length"),
        [
            ({"limit": 2}, 2),
            ({"limit": 3}, 3),
            ({"limit": 4, "index": 1}, 4),
        ],
    )
    def test_search_pagination(self, client, params, expected_length):
        result = client.search("Billy Jean", **params)
        assert isinstance(result, list)
        assert len(result) <= expected_length

    def test_search_strict(self, client):
        result = client.search("Soliloquy", strict=True)
        assert isinstance(result, list)
        assert all(isinstance(r, deezer.resources.Track) for r in result)
        assert result[0].title == "Soliloquy"

    @pytest.mark.parametrize(
        "ordering",
        [
            "RANKING",
            "TRACK_ASC",
            "TRACK_DESC",
            "ARTIST_ASC",
            "ARTIST_DESC",
            "ALBUM_ASC",
            "ALBUM_DESC",
            "RATING_ASC",
            "RATING_DESC",
            "DURATION_ASC",
            "DURATION_DESC",
        ],
    )
    def test_search_results_ordering(self, client, ordering):
        result = client.search("Soliloquy", ordering=ordering)
        assert isinstance(result, list)
        assert all(isinstance(r, deezer.resources.Track) for r in result)
        assert result[0].title == "Soliloquy"

    def test_search_advanced_simple(self, client):
        """Test advanced search with one term"""
        result = client.search(artist="Lou Doillon")
        assert isinstance(result, list)
        assert result[0].title == "Too much"

    def test_search_advanced_multiple(self, client):
        """Test advanced search with two term"""
        result = client.search(artist="Lou Doillon", album="Lay Low")
        assert isinstance(result, list)
        assert result[0].title == "Where To Start"

    def test_search_albums(self, client):
        """Test search for albums"""
        result = client.search_albums("Daft Punk")
        assert isinstance(result, list)
        assert all(isinstance(r, deezer.resources.Album) for r in result)
        assert result[0].title == "Discovery"

    def test_search_artists(self, client):
        """Test search for artists"""
        result = client.search_artists("Daft Punk")
        assert isinstance(result, list)
        assert all(isinstance(r, deezer.resources.Artist) for r in result)
        assert result[0].name == "Daft Punk"

    @pytest.mark.parametrize(
        ("header_value", "expected_name"),
        [
            ("fr", "Chanson fran\u00e7aise"),
            ("ja", "\u30d5\u30ec\u30f3\u30c1\u30fb\u30b7\u30e3\u30f3\u30bd\u30f3"),
        ],
        ids=["fr", "ja"],
    )
    def test_with_language_header(self, header_value, expected_name):
        """Get localised content with Accept-Language header."""
        client_fr = deezer.Client(headers={"Accept-Language": header_value})
        genre = client_fr.get_genre(52)
        assert isinstance(genre, deezer.resources.Genre)
        assert genre.name == expected_name

    @pytest.mark.parametrize(
        ("json", "expected_type"),
        [
            ({"name": "Unknown", "type": "unknown-type"}, deezer.resources.Resource),
            ({"title": "Album", "type": "album"}, deezer.resources.Album),
            ({"name": "Artist", "type": "artist"}, deezer.resources.Artist),
            ({"title": "Episode", "type": "episode"}, deezer.resources.Episode),
            ({"name": "Genre", "type": "genre"}, deezer.resources.Genre),
            ({"title": "Playlist", "type": "playlist"}, deezer.resources.Playlist),
            ({"title": "Podcast", "type": "podcast"}, deezer.resources.Podcast),
            ({"title": "Radio", "type": "radio"}, deezer.resources.Radio),
            ({"title": "Track", "type": "track"}, deezer.resources.Track),
            ({"name": "User", "type": "user"}, deezer.resources.User),
        ],
        ids=[
            "unknown",
            "album",
            "artist",
            # chart not tested here as isn't returned with "type":"chart"
            "episode",
            "genre",
            "playlist",
            "podcast",
            "radio",
            "track",
            "user",
        ],
    )
    def test_process_json_types(self, client, json, expected_type):
        result = client._process_json(json)
        assert type(result) == expected_type

    def test_rate_album(self, client_token):
        result = client_token.rate_album(302127, 4)
        assert result is True

    def test_rate_album_error(self, client):
        with pytest.raises(DeezerErrorResponse):
            client.rate_album(302127, 4)
