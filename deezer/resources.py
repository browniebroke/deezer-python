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
        self.client = client
        self.json = json
        for key in json:
            setattr(self, key, json[key])

    def __repr__(self):
        name = getattr(self, 'name', getattr(self, 'title', None))
        if name is not None:
            return '<%s: %s>' % (self.__class__.__name__,
                                 self.client.make_str(name))
        return super(Resource, self).__repr__()

    def get_relation(self, relation, **kwargs):
        """
        Generic method to load the relation from any resource.

        Query the client with the object's known parameters
        and try to retrieve the provided relation type. This
        is not meant to be used directly by a client, it's more
        a helper method for the child objects.
        """
        # object_t = self.__class__.__name__.lower()
        # pylint: disable=E1101
        return self.client.get_object(self.type, self.id, relation, **kwargs)


class Album(Resource):
    """To access an album resource."""

    def __init__(self, client, json):
        super(Album, self).__init__(client, json)

    def get_artist(self):
        """
        Return the :mod:`Artist <deezer.resources.Artist>` of the album
        """
        # pylint: disable=E1101
        return self.artist


class Artist(Resource):
    """To access an artist."""

    def __init__(self, client, json):
        super(Artist, self).__init__(client, json)


class Genre(Resource):
    """To access a genre."""

    def __init__(self, client, json):
        super(Genre, self).__init__(client, json)


class Track(Resource):
    """To access a track."""

    def __init__(self, client, json):
        super(Track, self).__init__(client, json)


class User(Resource):
    """To access a user."""

    def __init__(self, client, json):
        super(User, self).__init__(client, json)


class Playlist(Resource):
    """To access a playlist."""

    def __init__(self, client, json):
        super(Playlist, self).__init__(client, json)


class Comment(Resource):
    """To access a comment."""

    def __init__(self, client, json):
        super(Comment, self).__init__(client, json)


class Radio(Resource):
    """To access a radio."""

    def __init__(self, client, json):
        super(Radio, self).__init__(client, json)
