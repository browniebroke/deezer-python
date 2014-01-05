from urllib2 import urlopen
import json

class Client(object):
    """A client for Deezer resourses"""

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
        """Create a client instance with the provided options. Options should
        be passed in as kwargs.
        """
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
        """Build the url with the appended request if provided
        the request must start by '/' otherwise an Exception will
        be raised"""
        if request and not request.startswith('/'):
            raise Exception
        return "%s%s%s" % (self.scheme, self.host, request)

    def object_url(self, type, id=None, options = []):
        """
        Build the url to query to access the object 
        """
        if self.output is not "json":
            options.append("output=%s" % self.output)
        if type not in self.objects_types:
            raise TypeError("%s is not a valid type" % type)
        base_url = self.url("/" + type + ("/%s" % id if id else ""))
        return base_url + ("?%s" % "&".join(options) if options else "")

    def get_object(self, type, id=None):
        """
        Query Deezer to get the actual object
        """
        response = urlopen(self.object_url(type, id))
        if self.output is "json":
            return json.load(response)
        else:
            return response.read()

    def get_album(self, id):
        """Get the album with the provided id"""
        return self.get_object("album", id)

    def get_artist(self, id):
        """Get the artist with the provided id"""
        return self.get_object("artist", id)

    def get_comment(self, id):
        """Get the comment with the provided id"""
        return self.get_object("comment", id)

    def get_genre(self, id=None):
        """Get the genre with the provided id
        Returns all genres if id is ommitted"""
        return self.get_object("genre", id)

    def get_playlist(self, id):
        """Get the playlist with the provided id"""
        return self.get_object("comment", id)

    def get_radio(self, id=None):
        """Get the radio with the provided id.
        Returns all radios if id is ommitted"""
        return self.get_object("radio", id)

    def get_track(self, id):
        """Get the track with the provided id"""
        return self.get_object("track", id)

    def get_user(self, id):
        """Get the user with the provided id"""
        return self.get_object("user", id)


