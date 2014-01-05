deezer-python
=============

A friendly wrapper around the [Deezer API](http://developers.deezer.com/api).

Installation
------------

Just download the tarball and use the package locally, I haven't tested installation using easy_install yet

Basic Use
---------

So far you can only retrieve the data for the public objects, as json or xml. Search is not yet implemented.

    >>> client = deezer.Client()
    >>> client.get_album(12)
    {u'available': False, u'rating': 0, u'nb_tracks': 0, u'title': u'Monkey Business', u'tracks': {u'data': []}, u'release_date': u'0000-00-00', u'artist': {u'picture': u'https://api.deezer.com/artist/12/image', u'id': 12, u'name': u'Black Eyed Peas'}, u'cover': u'https://api.deezer.com/album/12/image', u'upc': u'_0602498822289', u'label': u'Universal Music Division Polydor', u'fans': 5, u'link': u'http://www.deezer.com/album/12', u'duration': 0, u'type': u'album', u'id': 12, u'genre_id': 18}

Authentication
--------------

Not supported yet, only public API accessible

Running Tests
-------------

The unit tests are using python unittest framework, just run:

    % python -m unittest discover
    ......
    ----------------------------------------------------------------------
    Ran 6 tests in 0.448s

    OK

Contributing
------------

Anyone is welcome to contribute by forking the repository and submitting pull requests. Just follow basic usage guide of Github, document your changes in this file or in the docstring, and make sure to write some test to verify your change.
