"""
Implements a client class to query the
`Deezer API <http://developers.deezer.com/api>`_
"""

from urllib2 import urlopen
import json
from deezer.resources import Album, Artist, Comment, Genre
from deezer.resources import Playlist, Radio, Track, User

class Client(object):
    """A client to retrieve some basic infos about Deezer resourses.

    Create a client instance with the provided options. Options should
    be passed in to the constructor as kwargs.

        >>> import deezer
        >>> client = deezer.Client(app_id='foo', app_secret='bar')

    This client provides several method to retrieve the content of most
    sort of Deezer objects, based on their json structure.
    """

    use_ssl = True
    host = "api.deezer.com"
    output = "json"

    objects_types = (
        "album",
        "artist",
        "comment",
        "editorial",
        # "folder", # need identification
        "genre",
        "playlist",
        "radio",
        "track",
        "user",
    )

    def __init__(self, **kwargs):
        super(Client, self).__init__()

        self.use_ssl = kwargs.get('use_ssl', self.use_ssl)
        self.host = kwargs.get('host', self.host)
        self.options = kwargs
        self._authorize_url = None

        self.app_id = kwargs.get('app_id')
        self.app_secret = kwargs.get('app_secret')
        self.access_token = kwargs.get('access_token')

    @property
    def scheme(self):
        """Get the http prefix for the address depending on the
        use_ssl attribute
        """
        return self.use_ssl and 'https://' or 'http://'

    def url(self, request=''):
        """Build the url with the appended request if provided.

        :raises ValueError: if the request does not start by '/'"""
        if request and not request.startswith('/'):
            raise ValueError
        return "%s%s%s" % (self.scheme, self.host, request)

    def object_url(self, object_t, object_id=None, relation=None, options=None):
        """
        Helper method to build the url to query to access the object
        passed as parameter

        :raises TypeError: if the object type is invalid
        """
        options = [options] if options else []
        if self.output is not "json":
            options.append("output=%s" % self.output)
        if object_t not in self.objects_types:
            raise TypeError("%s is not a valid type" % object_t)
        request = "/" + object_t
        if object_id:
            request += "/%s" % object_id
            if relation:
                request += "/%s" % relation
        base_url = self.url(request)
        return base_url + ("?%s" % "&".join(options) if options else "")

    def get_object(self, object_t, object_id=None, relation=None):
        """
        Actually query the Deezer API to retrieve the object

        :returns: json dictionnary or raw string if other
                  format requested
        """
        response = urlopen(self.object_url(object_t, object_id, relation))
        if self.output is "json":
            return json.load(response)
        else:
            return response.read()

    def get_album(self, object_id):
        """Get the album with the provided id

        :returns: an :class:`~deezer.resources.Album` object"""
        jsn = self.get_object("album", object_id)
        return Album(self, jsn)

    def get_artist(self, object_id):
        """Get the artist with the provided id

        :returns: an :class:`~deezer.resources.Artist` object"""
        jsn = self.get_object("artist", object_id)
        return Artist(self, jsn)

    def get_comment(self, object_id):
        """Get the comment with the provided id

        :returns: a :class:`~deezer.resources.Comment` object"""
        jsn = self.get_object("comment", object_id)
        return Comment(self, jsn)

    def get_genre(self, object_id):
        """Get the genre with the provided id

        :returns: a :class:`~deezer.resources.Genre` object"""
        jsn = self.get_object("genre", object_id)
        return Genre(self, jsn)

    def get_genres(self):
        """
        Returns a list of :class:`~deezer.resources.Genre` objects.
        """
        jsn = self.get_object("genre")
        ret = []
        for genre in jsn["data"]:
            ret.append(Genre(self, genre))
        return ret


    def get_playlist(self, object_id):
        """Get the playlist with the provided id

        :returns: a :class:`~deezer.resources.Playlist` object"""
        jsn = self.get_object("playlist", object_id)
        return Playlist(self, jsn)

    def get_radio(self, object_id=None):
        """Get the radio with the provided id.

        :returns: a :class:`~deezer.resources.Radio` object"""
        jsn = self.get_object("radio", object_id)
        return Radio(self, jsn)

    def get_track(self, object_id):
        """Get the track with the provided id

        :returns: a :class:`~deezer.resources.Track` object"""
        jsn = self.get_object("track", object_id)
        return Track(self, jsn)

    def get_user(self, object_id):
        """Get the user with the provided id

        :returns: a :class:`~deezer.resources.User` object"""
        jsn = self.get_object("user", object_id)
        return User(self, jsn)


