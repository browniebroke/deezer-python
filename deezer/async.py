"""
Implements an async tornado client class to query the
`Deezer API <http://developers.deezer.com/api>`_
"""
import json
import logging
from tornado.gen import coroutine, Return
from tornado.httpclient import AsyncHTTPClient
from deezer.client import Client
from deezer.resources import Album, Artist, Comment, Genre
from deezer.resources import Playlist, Radio, Track, User


class AsyncClient(Client):
    """
    An async client to retrieve some basic infos about Deezer resourses.

    Create a client instance with the provided options. Options should
    be passed in to the constructor as kwargs.

        >>> import deezer
        >>> client = deezer.AsyncClient(app_id='foo', app_secret='bar')

    This client provides several method to retrieve the content of most
    sort of Deezer objects, based on their json structure.
    """
    def __init__(self, *args, **kwargs):
        super(AsyncClient, self).__init__(*args, **kwargs)
        max_clients = kwargs.get('max_clients', 2)
        self._async_client = AsyncHTTPClient(max_clients=max_clients)

    @coroutine
    def get_object(self, object_t, object_id=None, relation=None, **kwargs):
        """
        Actually query the Deezer API to retrieve the object

        :returns: json dictionnary or raw string if other
                  format requested
        """
        url = self.object_url(object_t, object_id, relation, **kwargs)
        logging.debug(url)
        response = yield self._async_client.fetch(url)
        resp_str = response.body.decode('utf-8')
        if self.output is 'json':
            raise Return(json.loads(resp_str))
        else:
            raise Return(resp_str)

    @coroutine
    def get_album(self, object_id):
        """
        Get the album with the provided id

        :returns: an :class:`~deezer.resources.Album` object
        """
        jsn = yield self.get_object('album', object_id)
        raise Return(Album(self, jsn))

    @coroutine
    def get_artist(self, object_id):
        """
        Get the artist with the provided id

        :returns: an :class:`~deezer.resources.Artist` object
        """
        jsn = yield self.get_object('artist', object_id)
        raise Return(Artist(self, jsn))

    @coroutine
    def get_comment(self, object_id):
        """
        Get the comment with the provided id

        :returns: a :class:`~deezer.resources.Comment` object
        """
        jsn = yield self.get_object('comment', object_id)
        raise Return(Comment(self, jsn))

    @coroutine
    def get_genre(self, object_id):
        """
        Get the genre with the provided id

        :returns: a :class:`~deezer.resources.Genre` object
        """
        jsn = yield self.get_object('genre', object_id)
        raise Return(Genre(self, jsn))

    @coroutine
    def get_genres(self):
        """
        Returns a list of :class:`~deezer.resources.Genre` objects.
        """
        jsn = yield self.get_object('genre')
        ret = [Genre(self, genre) for genre in jsn['data']]
        raise Return(ret)

    @coroutine
    def get_playlist(self, object_id):
        """
        Get the playlist with the provided id

        :returns: a :class:`~deezer.resources.Playlist` object
        """
        jsn = yield self.get_object('playlist', object_id)
        raise Return(Playlist(self, jsn))

    @coroutine
    def get_radio(self, object_id=None):
        """
        Get the radio with the provided id.

        :returns: a :class:`~deezer.resources.Radio` object
        """
        jsn = yield self.get_object('radio', object_id)
        raise Return(Radio(self, jsn))

    @coroutine
    def get_track(self, object_id):
        """
        Get the track with the provided id

        :returns: a :class:`~deezer.resources.Track` object
        """
        jsn = yield self.get_object('track', object_id)
        raise Return(Track(self, jsn))

    @coroutine
    def get_user(self, object_id):
        """
        Get the user with the provided id

        :returns: a :class:`~deezer.resources.User` object
        """
        jsn = yield self.get_object('user', object_id)
        raise Return(User(self, jsn))

    @coroutine
    def _get_relation(self, object_t, object_id, relation, **kwargs):
        """
        Generic method to load the relation from any resource.
        Query the client with the object's known parameters
        and try to retrieve the provided relation type. This
        is not meant to be used directly by a client, it's more
        a helper method for the child objects.

        :returns: list of resource objects
        """
        jsn = yield self.get_object(object_t, object_id, relation, **kwargs)
        raise Return(self._process_relation(jsn))
