from __future__ import annotations

import pytest

import deezer

pytestmark = pytest.mark.vcr


class TestGenre:
    @pytest.fixture
    def electro(self, client):
        return client.get_genre(106)

    def test_attributes(self, electro):
        assert hasattr(electro, "name")
        assert isinstance(electro, deezer.Genre)
        assert repr(electro) == "<Genre: Electro>"

    def test_get_artists(self, electro):
        artists = electro.get_artists()
        assert isinstance(artists, list)
        assert len(artists) == 48
        artist = artists[0]
        assert isinstance(artist, deezer.Artist)
        assert repr(artist) == "<Artist: Major Lazer>"

    def test_get_podcasts(self, client):
        technology = client.get_genre(232)
        podcasts = technology.get_podcasts()
        assert isinstance(podcasts, deezer.PaginatedList)
        podcast = podcasts[0]
        assert isinstance(podcast, deezer.Podcast)
        assert repr(podcast) == "<Podcast: Le rendez-vous Tech>"
        assert len(podcasts) == 15

    def test_get_radios(self, electro):
        radios = electro.get_radios()
        assert isinstance(radios, list)
        assert len(radios) == 32
        radio = radios[0]
        assert isinstance(radio, deezer.Radio)
        assert repr(radio) == "<Radio: Electro Swing>"
