"""
Implements a client class to query the `Deezer API <http://developers.deezer.com/api>`_
"""

from urllib2 import urlopen
import json
from resources import Album, Artist, Comment

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
        self.output = kwargs.get('output', self.output)
        self.scheme = self.use_ssl and 'https://' or 'http://'
        self.options = kwargs
        self._authorize_url = None

        self.app_id = kwargs.get('app_id')
        self.app_secret = kwargs.get('app_secret')
        self.access_token = kwargs.get('access_token')

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

        :returns: an `Album <#deezer.resources.Album>`_ object"""
        json = self.get_object("album", object_id)
        return Album(self, json)

    def get_artist(self, object_id):
        """Get the artist with the provided id

        :returns: an `Artist <#deezer.resources.Artist>`_ object"""
        json = self.get_object("artist", object_id)
        return Artist(self, json)

    def get_comment(self, object_id):
        """Get the comment with the provided id

        :returns: a `Comment <#deezer.resources.Comment>`_ object"""
        json = self.get_object("comment", object_id)
        return Comment(self, json)

    def get_genre(self, object_id):
        """Get the genre with the provided id

        :returns: a `Genre <#deezer.resources.Genre>`_ object"""
        json = self.get_object("genre", object_id)
        return Genre(json)

    def get_genres(self):
        """
        Returns a list of `Genre <#deezer.resources.Genre>`_ objects.
        """
        json = self.get_object("genre")
        ret = []
        for genre in json["data"]:
            ret.append(Genre(self, genre))
        return ret


    def get_playlist(self, object_id):
        """Get the playlist with the provided id

        :returns: same return format as `get_object <#deezer.client.Client.get_object>`_"""
        return self.get_object("comment", object_id)

    def get_radio(self, object_id=None):
        """Get the radio with the provided id.
        Returns all radios if id is ommitted

        :returns: same return format as `get_object <#deezer.client.Client.get_object>`_"""
        return self.get_object("radio", object_id)

    def get_track(self, object_id):
        """Get the track with the provided id

        :returns: same return format as `get_object <#deezer.client.Client.get_object>`_"""
        return self.get_object("track", object_id)

    def get_user(self, object_id):
        """Get the user with the provided id

        :returns: same return format as `get_object <#deezer.client.Client.get_object>`_"""
        return self.get_object("user", object_id)


