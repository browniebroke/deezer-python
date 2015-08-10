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
            return '<{0}: {1}>'.format(self.__class__.__name__,
                                       self.client.make_str(name))
        return super(Resource, self).__repr__()

    def asdict(self):
        """
        Convert resource to dictionary
        """
        result = {}
        for key in self._fields:
            value = getattr(self, key)
            if isinstance(value, list):
                value = [i.asdict()
                         if isinstance(i, Resource) else i
                         for i in value]
            if isinstance(value, Resource):
                value = value.asdict()
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
        return self.client.get_object(self.type, self.id, relation,
                                      self, **kwargs)

    def get_artist(self):
        """
        :returns: the :mod:`Artist <deezer.resources.Artist>` of the resource
        :raises AssertionError: if the object is not album or track
        """
        # pylint: disable=E1101
        assert isinstance(self, (Album, Track))
        return self.client.get_artist(self.artist.id)


class Album(Resource):
    """To access an album resource."""

    def get_tracks(self):
        """
        Get a list of album's tracks.
        :returns: list of :mod:`Track <deezer.resources.Track>` instances
        """
        return self.get_relation('tracks')


class Artist(Resource):
    """To access an artist."""

    def get_top(self):
        """
        Get the top 5 tracks of an artist.
        :returns: list of :mod:`Track <deezer.resources.Track>` instances
        """
        return self.get_relation('top')

    def get_related(self):
        """
        Get a list of related artists.
        :returns: list of :mod:`Artist <deezer.resources.Artist>` instances
        """
        return self.get_relation('related')

    def get_radio(self):
        """
        :returns: list of :mod:`Track <deezer.resources.Track>` instances
        """
        return self.get_relation('radio')

    def get_albums(self):
        """
        Get a list of artist's albums.
        :returns: list of :mod:`Album <deezer.resources.Album>` instances
        """
        return self.get_relation('albums')


class Genre(Resource):
    """To access a genre."""

    def get_artists(self):
        """
        Get all artists for a genre.
        :returns: list of :mod:`Artist <deezer.resources.Artist>` instances
        """
        return self.get_relation('artists')

    def get_radios(self):
        """
        Get all radios for a genre.
        :returns: list of :mod:`Radio <deezer.resources.Track>` instances
        """
        return self.get_relation('radios')


class Track(Resource):
    """To access a track."""

    def get_album(self):
        """
        :returns: the :mod:`Album <deezer.resources.Album>` instance
        """
        return self.client.get_album(self.album.id)


class User(Resource):
    """To access a user."""


class Playlist(Resource):
    """To access a playlist."""


class Comment(Resource):
    """To access a comment."""


class Radio(Resource):
    """To access a radio."""

    def get_tracks(self):
        """
        Get first 40 tracks in the radio
        :returns: list of  :mod:`Track <deezer.resources.Track>` instances
        """
        return self.get_relation('tracks')
