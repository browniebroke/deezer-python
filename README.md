deezer-python
=============

A friendly wrapper around the [Deezer API](http://developers.deezer.com/api).

Installation
------------

Just download the tarball and use the package locally, I haven't tested installation using easy_install yet

Basic Use
---------

So far you can only retrieve the data for the public objects, for which no login is required. The objects are translated to python resources, which are basically python objects encapsulating the json dictionary returned by the API. Search is not yet implemented.

    >>> client = deezer.Client()
    >>> client.get_album(12).title
    u'Monkey Business'
    
See the whole API on the [Sphinx](http://sphinx-doc.org/) generated [documentation](http://deezer-python.readthedocs.org/).

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
