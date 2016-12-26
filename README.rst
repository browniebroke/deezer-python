Deezer Python Client
====================

|build| |coverage| |docs| |pypi| |landscape| |pyversions| |license|

A friendly wrapper around the `Deezer API`_.

Installation
------------

The package is published on the `Python index <https://pypi.python.org/pypi/deezer-python/>`_ simply run the following:

::

    pip install deezer-python

And that's it!

Basic Use
---------

So far you can only retrieve the data for the public objects, for which no login is required.
The objects are translated to python resources, which are basically python objects encapsulating
the json dictionary returned by the API.

.. code-block:: python

    >>> client = deezer.Client()
    >>> client.get_album(12).title
    u'Monkey Business'

You also can use AsyncClient with tornado.

.. code-block:: python

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

Not supported by this package. There are excellent other python modules to
handle that. There is the excellent `Python Social Auth`_, it doesn't support
Deezer, but it's very easily extensible to support it, and if you do write a
back-end for it, I'd encourage you to submit a pull request there.


.. |build| image:: https://travis-ci.org/browniebroke/deezer-python.svg
    :target: https://travis-ci.org/browniebroke/deezer-python
    :alt: Build status
.. |coverage| image:: https://codecov.io/gh/browniebroke/deezer-python/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/browniebroke/deezer-python
    :alt: Test coverage percentage
.. |docs| image:: https://readthedocs.org/projects/deezer-python/badge/?version=latest
    :target: https://deezer-python.readthedocs.io
    :alt: Documentation Status
.. |pypi| image:: https://badge.fury.io/py/deezer-python.svg
    :target: http://badge.fury.io/py/deezer-python
    :alt: PyPi Status
.. |landscape| image:: https://landscape.io/github/browniebroke/deezer-python/master/landscape.svg?style=flat
    :target: https://landscape.io/github/browniebroke/deezer-python/master
    :alt: Code Health
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/deezer-python.svg
.. |license| image:: https://img.shields.io/pypi/l/deezer-python.svg
.. _Deezer API: http://developers.deezer.com/api
.. _Sphinx: http://sphinx-doc.org/
.. _documentation: http://deezer-python.readthedocs.io/
.. _Python Social Auth: https://github.com/python-social-auth
