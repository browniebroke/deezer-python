Deezer Python Client
====================

|build| |win_build| |coverage| |codeclimate| |black|

|docs| |pypi| |pyversions| |license|

A friendly wrapper around the `Deezer API`_.

Installation
------------

The package is published on `PyPI <https://pypi.org/project/deezer-python/>`_ and can be installed by running:

::

    pip install deezer-python

Basic Use
---------

So far you can only retrieve the data for the public objects, for which no login is required.
The objects are translated to python resources, which are basically python objects encapsulating
the json dictionary returned by the API.

.. code-block:: python

    >>> client = deezer.Client()
    >>> client.get_album(12).title
    u'Monkey Business'

See the whole API reference on the `Sphinx`_ generated `documentation`_.

Asynchronous client
```````````````````

You also can use an ``AsyncClient`` with tornado, which requires an optional dependency. You should
install with ``pip install deezer-python[tornado]``. Then, making requests look like:

.. code-block:: python

    >>> from tornado.gen import coroutine
    >>> from tornado.ioloop import IOLoop
    >>> from deezer.contrib.tornado import AsyncClient
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

Authentication
--------------

Not supported by this package. There are excellent other python modules to
handle that. There is the excellent `Python Social Auth`_, which supports
Deezer authentication.

.. |build| image:: https://travis-ci.org/browniebroke/deezer-python.svg
    :target: https://travis-ci.org/browniebroke/deezer-python
    :alt: Build status
.. |win_build| image:: https://ci.appveyor.com/api/projects/status/l5vb8sl9ey12s3nd?svg=true
    :target: https://ci.appveyor.com/project/browniebroke/deezer-python
    :alt: Build status
.. |codeclimate| image:: https://api.codeclimate.com/v1/badges/bfbf562a06742972c694/maintainability
   :target: https://codeclimate.com/github/browniebroke/deezer-python/maintainability
   :alt: Maintainability
.. |coverage| image:: https://codecov.io/gh/browniebroke/deezer-python/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/browniebroke/deezer-python
    :alt: Test coverage percentage
.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
.. |docs| image:: https://readthedocs.org/projects/deezer-python/badge/?version=latest
    :target: https://deezer-python.readthedocs.io
    :alt: Documentation Status
.. |pypi| image:: https://badge.fury.io/py/deezer-python.svg
    :target: http://badge.fury.io/py/deezer-python
    :alt: PyPi Status
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/deezer-python.svg
.. |license| image:: https://img.shields.io/pypi/l/deezer-python.svg
.. _Deezer API: http://developers.deezer.com/api
.. _Sphinx: http://sphinx-doc.org/
.. _documentation: http://deezer-python.readthedocs.io/
.. _Python Social Auth: https://github.com/python-social-auth
