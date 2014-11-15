deezer-python |build-status| |coverage-status| |docs|
=====================================================

A friendly wrapper around the `Deezer API`_.

Installation
------------

Just download the tarball and use the package locally, I haven't tested installation using easy_install yet

Basic Use
---------

So far you can only retrieve the data for the public objects, for which no login is required.
The objects are translated to python resources, which are basically python objects encapsulating 
the json dictionary returned by the API. Search is not yet implemented.


    >>> client = deezer.Client()
    >>> client.get_album(12).title
    u'Monkey Business'

You also can use AsyncClient with tornado.


    >>> from tornado.gen import coroutine
    >>> from tornado.ioloop import IOLoop
    >>> from deezer import AsyncClient
    >>>
    >>>
    >>> @coroutine
    ... def main():
    ...     client = AsyncClient()
    ...     album = yield client.get_album(12)
    ...     print(album.title)
    ...
    >>> IOLoop.instance().run_sync(main)
    Monkey Business

See the whole API on the `Sphinx`_ generated `documentation`_.

Authentication
--------------

Not supported yet, only public API accessible

Running Tests
-------------

The unit tests are using python unittest framework, just run:

::

    % python -m unittest discover
    ......
    ----------------------------------------------------------------------
    Ran 6 tests in 0.448s

    OK


.. |build-status| image:: https://travis-ci.org/browniebroke/deezer-python.png
    :target: https://travis-ci.org/browniebroke/deezer-python
    :alt: Build status
.. |coverage-status| image:: https://coveralls.io/repos/browniebroke/deezer-python/badge.png
    :target: https://coveralls.io/r/browniebroke/deezer-python
    :alt: Test coverage percentage
.. |docs| image:: https://readthedocs.org/projects/deezer-python/badge/?version=latest
    :target: http://deezer-python.readthedocs.org/
    :alt: Documentation Status
.. _Deezer API: http://developers.deezer.com/api
.. _Sphinx: http://sphinx-doc.org/
.. _documentation: http://deezer-python.readthedocs.org/
