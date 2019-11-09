"""
Implements a client class to query the
`Deezer API <http://developers.deezer.com/api>`_
"""
from urllib.parse import urlencode

import requests

from deezer.resources import (
    Album,
    Artist,
    Chart,
    Comment,
    Genre,
    Playlist,
    Radio,
    Track,
    User,
)
from deezer.utils import SortedDict


class Client:
    """
    A client to retrieve some basic infos about Deezer resourses.

    Create a client instance with the provided options. Options should
    be passed in to the constructor as kwargs.

        >>> import deezer
        >>> client = deezer.Client(app_id='foo', app_secret='bar')

    This client provides several method to retrieve the content of most
    sort of Deezer objects, based on their json structure.

    Headers can be forced by using the ``headers`` kwarg.
    For example, use ``Accept-Language`` header to force the output language.

        >>> import deezer
        >>> client = deezer.Client(headers={'Accept-Language': 'fr'})
    """

    use_ssl = True
    host = "api.deezer.com"

    objects_types = {
        "album": Album,
        "artist": Artist,
        "comment": Comment,
        "editorial": None,
        # 'folder': None, # need identification
        "genre": Genre,
        "playlist": Playlist,
        "radio": Radio,
        "search": None,
        "track": Track,
        "user": User,
        "chart": Chart,
    }

    def __init__(self, **kwargs):
        super().__init__()

        self.use_ssl = kwargs.get("use_ssl", self.use_ssl)
        self.host = kwargs.get("host", self.host)
        self.session = requests.Session()

        # Do not compress the response: to be readable in tests (cassettes)
        if kwargs.get("do_not_compress_reponse"):
            self.session.headers.update({"Accept-Encoding": "identity"})

        # Headers
        if kwargs.get("headers"):
            self.session.headers.update(kwargs.get("headers"))

        self.options = kwargs
        self._authorize_url = None

        self.app_id = kwargs.get("app_id")
        self.app_secret = kwargs.get("app_secret")
        self.access_token = kwargs.get("access_token")

    def _process_json(self, item, parent=None):
        """
        Recursively convert dictionary
        to :class:`~deezer.resources.Resource` object

        :returns: instance of :class:`~deezer.resources.Resource`
        """
        if "data" in item:
            return [self._process_json(i, parent) for i in item["data"]]

        result = {}
        for key, value in item.items():
            if isinstance(value, dict) and ("type" in value or "data" in value):
                value = self._process_json(value, parent)
            result[key] = value
        if parent is not None and hasattr(parent, "type"):
            result[parent.type] = parent

        if "type" in result:
            object_class = self.objects_types[result["type"]]
        else:
            object_class = self.objects_types[parent]
        return object_class(self, result)

    @property
    def scheme(self):
        """
        Get the http prefix for the address depending on the use_ssl attribute
        """
        return self.use_ssl and "https" or "http"

    def url(self, request=""):
        """Build the url with the appended request if provided."""
        if request.startswith("/"):
            request = request[1:]
        return "{}://{}/{}".format(self.scheme, self.host, request)

    def object_url(self, object_t, object_id=None, relation=None, **kwargs):
        """
        Helper method to build the url to query to access the object
        passed as parameter

        :raises TypeError: if the object type is invalid
        """
        if object_t not in self.objects_types:
            raise TypeError("{} is not a valid type".format(object_t))
        request_items = (
            str(item) for item in [object_t, object_id, relation] if item is not None
        )
        request = "/".join(request_items)
        base_url = self.url(request)
        if self.access_token is not None:
            kwargs["access_token"] = str(self.access_token)
        if kwargs:
            for key, value in kwargs.items():
                if not isinstance(value, str):
                    kwargs[key] = str(value)
            # kwargs are sorted (for consistent tests between Python < 3.7 and >= 3.7)
            sorted_kwargs = SortedDict.from_dict(kwargs)
            result = "{}?{}".format(base_url, urlencode(sorted_kwargs))
        else:
            result = base_url
        return result

    def get_object(
        self, object_t, object_id=None, relation=None, parent=None, **kwargs
    ):
        """
        Actually query the Deezer API to retrieve the object

        :returns: json dictionary
        """
        url = self.object_url(object_t, object_id, relation, **kwargs)
        response = self.session.get(url)
        json = response.json()
        if "error" in json:
            raise ValueError(
                "API request return error for object: %s id: %s" % (object_t, object_id)
            )
        return self._process_json(json, parent)

    def get_chart(self, relation=None, index=0, limit=10, **kwargs):
        """
        Get chart

        :returns: a list of :class:`~deezer.resources.Resource` objects.
        """
        return self.get_object(
            "chart", object_id="0", relation=relation, parent="chart", **kwargs
        )

    def get_album(self, object_id, relation=None, **kwargs):
        """
        Get the album with the provided id

        :returns: an :class:`~deezer.resources.Album` object
        """
        return self.get_object("album", object_id, relation=relation, **kwargs)

    def get_artist(self, object_id, relation=None, **kwargs):
        """
        Get the artist with the provided id

        :returns: an :class:`~deezer.resources.Artist` object
        """
        return self.get_object("artist", object_id, relation=relation, **kwargs)

    def get_comment(self, object_id):
        """
        Get the comment with the provided id

        :returns: a :class:`~deezer.resources.Comment` object
        """
        return self.get_object("comment", object_id)

    def get_genre(self, object_id):
        """
        Get the genre with the provided id

        :returns: a :class:`~deezer.resources.Genre` object
        """
        return self.get_object("genre", object_id)

    def get_genres(self):
        """
        :returns: a list of :class:`~deezer.resources.Genre` objects.
        """
        return self.get_object("genre")

    def get_playlist(self, object_id):
        """
        Get the playlist with the provided id

        :returns: a :class:`~deezer.resources.Playlist` object
        """
        return self.get_object("playlist", object_id)

    def get_radio(self, object_id=None):
        """
        Get the radio with the provided id.

        :returns: a :class:`~deezer.resources.Radio` object
        """
        return self.get_object("radio", object_id)

    def get_radios(self):
        """
        Get a list of radios.

        :returns: a list of :class:`~deezer.resources.Radio` objects
        """
        return self.get_object("radio")

    def get_radios_top(self):
        """
        Get the top radios (5 radios).

        :returns: a :class:`~deezer.resources.Radio` object
        """
        return self.get_object("radio", relation="top")

    def get_track(self, object_id):
        """
        Get the track with the provided id

        :returns: a :class:`~deezer.resources.Track` object
        """
        return self.get_object("track", object_id)

    def get_user(self, object_id):
        """
        Get the user with the provided id

        :returns: a :class:`~deezer.resources.User` object
        """
        return self.get_object("user", object_id)

    def search(self, query, relation=None, index=0, limit=25, **kwargs):
        """
        Search track, album, artist or user

        :returns: a list of :class:`~deezer.resources.Resource` objects.
        """
        return self.get_object(
            "search", relation=relation, q=query, index=index, limit=limit, **kwargs
        )

    def advanced_search(self, terms, relation=None, index=0, limit=25, **kwargs):
        """
        Advanced search of track, album or artist.

        See `Search section of Deezer API
        <https://developers.deezer.com/api/search>`_ for search terms.

        :returns: a list of :class:`~deezer.resources.Resource` objects.

        >>> client.advanced_search({"artist": "Daft Punk", "album": "Homework"})
        >>> client.advanced_search({"artist": "Daft Punk", "album": "Homework"},
        ...                        relation="track")
        """
        if not isinstance(terms, dict):
            raise TypeError("terms must be a dict")
        # terms are sorted (for consistent tests between Python < 3.7 and >= 3.7)
        query = " ".join(sorted(['{}:"{}"'.format(k, v) for (k, v) in terms.items()]))
        return self.get_object(
            "search", relation=relation, q=query, index=index, limit=limit, **kwargs
        )
