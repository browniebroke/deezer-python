"""
Module to implement the various types of resources that
can be found in the API.
"""


class Resource(object):
    """
    Base class for any resource.

    It is mainly responsible of passing a reference to the client
    to this class when instantiated, and transmit the json data into
    attributes
    """

    def __init__(self, client, json):
        self._fields = tuple(json.keys())
        self.client = client
        for key in json:
            setattr(self, key, json[key])

    def __repr__(self):
        name = getattr(self, 'name', getattr(self, 'title', None))
        if name is not None:
            return '<%s: %s>' % (self.__class__.__name__,
                                 self.client.make_str(name))
        return super(Resource, self).__repr__()

    def _asdict(self):
        result = {}
        for key in self._fields:
            value = getattr(self, key)
            if isinstance(value, list):
                value = [i._asdict()
                         if isinstance(i, Resource) else i
                         for i in value]
            if isinstance(value, Resource):
                value = value._asdict()
            result[key] = value
        return result

    def get_relation(self, relation, **kwargs):
        """
        Generic method to load the relation from any resource.

        Query the client with the object's known parameters
        and try to retrieve the provided relation type. This
        is not meant to be used directly by a client, it's more
        a helper method for the child objects.
        """
        # pylint: disable=E1101
        return self.client.get_object(self.type, self.id, relation, **kwargs)

    def get_artist(self):
        """
        :returns: the :mod:`Artist <deezer.resources.Artist>` of the resource
        :raises AssertionError: if the object is not album or track
        """
        # pylint: disable=E1101
        assert isinstance(self, (Album, Track))
        return self.client.get_artist(self.artist.id)

    def get_album(self):
        """
        :returns: the :mod:`Album <deezer.resources.Album>` of the resource
        :raises AssertionError: if the object is not artist or track
        """
        # pylint: disable=E1101
        assert isinstance(self, (Artist, Track))
        return self.client.get_album(self.album.id)

    def get_tracks(self):
        """
        :returns: list of  :mod:`Track <deezer.resources.Track>` instances
        :raises AssertionError: if the object is not artist or album
        """
        assert isinstance(self, (Artist, Album))
        if isinstance(self, Artist):
            return self.get_relation('top')
        if isinstance(self, Album):
            return self.get_relation('tracks')


class Album(Resource):
    """To access an album resource."""
    pass


class Artist(Resource):
    """To access an artist."""
    pass


class Genre(Resource):
    """To access a genre."""
    pass


class Track(Resource):
    """To access a track."""
    pass


class User(Resource):
    """To access a user."""
    pass


class Playlist(Resource):
    """To access a playlist."""
    pass


class Comment(Resource):
    """To access a comment."""
    pass


class Radio(Resource):
    """To access a radio."""
    pass
