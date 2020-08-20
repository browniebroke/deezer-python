import pytest

import deezer

pytestmark = pytest.mark.vcr


class TestClient:
    def test_access_token_set(self, client):
        """Test that access token is set on the client."""
        client.access_token = "token"
        assert client.access_token, "token"
        assert (
            client.object_url("user", "me")
            == "https://api.deezer.com/user/me?access_token=token"
        )

    def test_no_compress_response(self):
        client = deezer.Client(do_not_compress_reponse=True)
        assert client.session.headers["Accept-Encoding"] == "identity"

    def test_kwargs_parsing_valid(self, client):
        assert client.app_id == "foo"
        assert client.app_secret == "bar"

    def test_ssl_enabled(self, client):
        assert client.scheme == "https"

    def test_unsecure_client(self):
        non_secure_client = deezer.Client(use_ssl=False)
        assert non_secure_client.scheme == "http"

    def test_url(self, client):
        """Test the url() method
        it should add / to the request if not present
        """
        client.url()
        user = client.url("/user")
        assert user == "https://api.deezer.com/user"
        user = client.url("user")
        assert user == "https://api.deezer.com/user"

    @pytest.mark.parametrize(
        ("args", "kwargs", "expected_output"),
        [
            (("album",), {}, "https://api.deezer.com/album"),
            (("album", 12,), {}, "https://api.deezer.com/album/12"),
            (("album", "12",), {}, "https://api.deezer.com/album/12"),
            (("album", "12", "artist",), {}, "https://api.deezer.com/album/12/artist"),
            (("album", "12", "artist",), {}, "https://api.deezer.com/album/12/artist"),
            (("album", "12"), {"limit": 1}, "https://api.deezer.com/album/12?limit=1"),
            (
                ("artist", "12", "albums"),
                {"limit": 1},
                "https://api.deezer.com/artist/12/albums?limit=1",
            ),
        ],
    )
    def test_object_url(self, client, args, kwargs, expected_output):
        assert client.object_url(*args, **kwargs) == expected_output

    def test_object_url_invalid_type(self, client):
        with pytest.raises(TypeError):
            client.object_url("foo")

    def test_get_album(self, client):
        """Test method to retrieve an album"""
        album = client.get_album(302127)
        assert isinstance(album, deezer.resources.Album)

    def test_no_album_raise(self, client):
        """Test method get_album for invalid value"""
        with pytest.raises(ValueError):
            client.get_album(-1)

    def test_get_artist(self, client):
        """Test methods to get an artist"""
        artist = client.get_artist(27)
        assert isinstance(artist, deezer.resources.Artist)

    def test_no_artist_raise(self, client):
        """Test method get_artist for invalid value"""
        with pytest.raises(ValueError):
            client.get_artist(-1)

    def test_chart(self, client):
        assert client.object_url("chart") == "https://api.deezer.com/chart"
        result = client.get_chart()
        assert isinstance(result, deezer.resources.Chart)

        assert isinstance(result.tracks[0], deezer.resources.Track)
        assert isinstance(result.albums[0], deezer.resources.Album)
        assert isinstance(result.artists[0], deezer.resources.Artist)
        assert isinstance(result.playlists[0], deezer.resources.Playlist)

    def test_chart_tracks(self, client):
        result = client.get_chart("tracks")
        assert isinstance(result, list)
        assert result[0].title == "Khapta"
        assert isinstance(result[0], deezer.resources.Track)

    def test_chart_albums(self, client):
        result = client.get_chart("albums")
        assert isinstance(result, list)
        assert result[0].title == "Lacrim"
        assert isinstance(result[0], deezer.resources.Album)

    def test_chart_artists(self, client):
        result = client.get_chart("artists")
        assert isinstance(result, list)
        assert result[0].name == "Lacrim"
        assert isinstance(result[0], deezer.resources.Artist)

    def test_chart_playlists(self, client):
        result = client.get_chart("playlists")
        assert isinstance(result, list)
        assert result[0].title == "Les titres du moment"
        assert isinstance(result[0], deezer.resources.Playlist)

    def test_get_comment(self, client):
        """Test methods to get a comment"""
        comment = client.get_comment(2772704)
        assert isinstance(comment, deezer.resources.Comment)

    def test_no_comment_raise(self, client):
        """Test method get_comment for invalid value"""
        with pytest.raises(ValueError):
            client.get_comment(-1)

    def test_get_episode(self, client):
        """Test methods to get an episode"""
        episode = client.get_episode(238455362)
        assert isinstance(episode, deezer.resources.Episode)

    def test_no_episode_raise(self, client):
        """Test method get_episode for invalid value"""
        with pytest.raises(ValueError):
            client.get_episode(-1)

    def test_get_genre(self, client):
        """Test methods to get a genre"""
        genre = client.get_genre(106)
        assert isinstance(genre, deezer.resources.Genre)

    def test_no_genre_raise(self, client):
        """Test method get_genre for invalid value"""
        with pytest.raises(ValueError):
            client.get_genre(-1)

    def test_get_genres(self, client):
        """Test methods to get several genres"""
        genres = client.get_genres()
        assert isinstance(genres, list)
        assert isinstance(genres[0], deezer.resources.Genre)

    def test_get_playlist(self, client):
        """Test methods to get a playlist"""
        playlist = client.get_playlist(908622995)
        assert isinstance(playlist, deezer.resources.Playlist)

    def test_no_playlist_raise(self, client):
        """Test method get_playlist for invalid value"""
        with pytest.raises(ValueError):
            client.get_playlist(-1)

    def test_get_podcast(self, client):
        """Test methods to get a podcast"""
        podcast = client.get_podcast(699612)
        assert isinstance(podcast, deezer.resources.Podcast)

    def test_no_podcast_raise(self, client):
        """Test method get_podcast for invalid value"""
        with pytest.raises(ValueError):
            client.get_podcast(-1)

    def test_get_radio(self, client):
        """Test methods to get a radio"""
        radio = client.get_radio(23261)
        assert isinstance(radio, deezer.resources.Radio)

    def test_no_radio_raise(self, client):
        """Test method get_radio for invalid value"""
        with pytest.raises(ValueError):
            client.get_radio(-1)

    def test_get_radios(self, client):
        """Test methods to get a radios"""
        radios = client.get_radios()
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
        with pytest.raises(ValueError):
            client.get_track(-1)

    def test_get_user(self, client):
        """Test methods to get a user"""
        user = client.get_user(359622)
        assert isinstance(user, deezer.resources.User)

    def test_no_user_raise(self, client):
        """Test method get_user for invalid value"""
        with pytest.raises(ValueError):
            client.get_user(-1)

    def test_options_1(self, client):
        """Test a query with extra arguments"""
        result = client.search("Billy Jean", limit=2)
        assert isinstance(result, list)
        assert len(result) <= 2

    def test_options_2(self, client):
        """Test a query with extra arguments"""
        result = client.search("Billy Jean", limit=2, index=1)
        assert isinstance(result, list)
        assert len(result) <= 2

    def test_search_simple(self, client):
        """Test search method"""
        assert (
            client.object_url("search", q="Soliloquy")
            == "https://api.deezer.com/search?q=Soliloquy"
        )
        result = client.search("Soliloquy")
        assert isinstance(result, list)
        assert result[0].title == "Too much"

    def test_search_with_relation(self, client):
        """Test search method with relation"""
        assert (
            client.object_url("search", relation="album", q="Daft Punk")
            == "https://api.deezer.com/search/album?q=Daft+Punk"
        )
        result = client.search("Daft Punk", "album")
        assert isinstance(result, list)
        assert result[0].title == "Random Access Memories"
        assert isinstance(result[0], deezer.resources.Album)

        result = client.search("Daft Punk", "album", "0", "1")
        assert isinstance(result, list)
        assert len(result) == 1
        assert result[0] != client.search("Daft Punk", "album", "1", "1")

    def test_advanced_search_simple(self, client):
        """Test advanced_search method: simple case with one term"""
        assert (
            client.object_url("search", q='artist:"Lou Doillon"')
            == "https://api.deezer.com/search?q=artist%3A%22Lou+Doillon%22"
        )
        result = client.advanced_search({"artist": "Lou Doillon"})
        assert isinstance(result, list)
        assert result[0].title == "Too much"

    def test_advanced_search_complex(self, client):
        """Test advanced_search method: complex case with two term"""
        assert client.object_url(
            "search", q='artist:"Lou Doillon" album:"Lay Low"'
        ) == (
            "https://api.deezer.com/search?"
            "q=artist%3A%22Lou+Doillon%22+album%3A%22Lay+Low%22"
        )
        result = client.advanced_search({"artist": "Lou Doillon", "album": "Lay Low"})
        assert isinstance(result, list)
        assert result[0].title == "Where To Start"

    def test_advanced_search_complex_with_relation(self, client):
        """Test advanced_search method: with relation"""
        # Two terms with a relation
        assert client.object_url(
            "search", relation="track", q='artist:"Lou Doillon" track:"Joke"'
        ) == (
            "https://api.deezer.com/search/track?"
            "q=artist%3A%22Lou+Doillon%22+track%3A%22Joke%22"
        )
        result = client.advanced_search(
            {"artist": "Lou Doillon", "track": "Joke"}, relation="track"
        )
        assert isinstance(result, list)
        assert result[0].title == "The joke"
        assert isinstance(result[0], deezer.resources.Track)

    def test_advanced_search_invalid(self, client):
        with pytest.raises(TypeError):
            client.advanced_search("Lou Doillon")

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
            ({"name": "Unknown", "type": "unknown-type"}, deezer.resources.Resource,),
            ({"title": "Album", "type": "album"}, deezer.resources.Album,),
            ({"name": "Artist", "type": "artist"}, deezer.resources.Artist,),
            ({"text": "Comment", "type": "comment"}, deezer.resources.Comment,),
            ({"title": "Episode", "type": "episode"}, deezer.resources.Episode,),
            ({"name": "Genre", "type": "genre"}, deezer.resources.Genre,),
            ({"title": "Playlist", "type": "playlist"}, deezer.resources.Playlist,),
            ({"title": "Podcast", "type": "podcast"}, deezer.resources.Podcast,),
            ({"title": "Radio", "type": "radio"}, deezer.resources.Radio,),
            ({"title": "Track", "type": "track"}, deezer.resources.Track,),
            ({"name": "User", "type": "user"}, deezer.resources.User,),
        ],
        ids=[
            "unknown",
            "album",
            "artist",
            # chart not tested here as isn't returned with "type":"chart"
            "comment",
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
