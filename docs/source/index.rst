Deezer python's documentation
=============================

.. automodule:: deezer

Deezer Python Client
====================

|build| |win_build| |coverage| |codeclimate| |black|

|docs| |pypi| |pyversions| |license| |loc|

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
    'Monkey Business'

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

.. |build| image:: https://img.shields.io/travis/browniebroke/deezer-python.svg?style=flat-square&logo=travis
    :target: https://travis-ci.org/browniebroke/deezer-python
    :alt: Build status
.. |win_build| image:: https://img.shields.io/appveyor/ci/browniebroke/deezer-python.svg?logo=appveyor&style=flat-square
    :target: https://ci.appveyor.com/project/browniebroke/deezer-python
    :alt: Build status
.. |codeclimate| image:: https://api.codeclimate.com/v1/badges/bfbf562a06742972c694/maintainability
   :target: https://codeclimate.com/github/browniebroke/deezer-python/maintainability
   :alt: Maintainability
.. |coverage| image:: https://img.shields.io/codecov/c/github/browniebroke/deezer-python.svg?logo=codecov&style=flat-square
    :target: https://codecov.io/gh/browniebroke/deezer-python
    :alt: Test coverage percentage
.. |black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/ambv/black
.. |docs| image:: https://img.shields.io/readthedocs/deezer-python.svg?logo=read-the-docs&style=flat-square
    :target: https://deezer-python.readthedocs.io
    :alt: Documentation Status
.. |pypi| image:: https://img.shields.io/pypi/v/deezer-python.svg?logo=python&logoColor=fff&style=flat-square
    :target: https://pypi.org/project/deezer-python/
    :alt: PyPi Status
.. |loc| image:: https://tokei.rs/b1/github/browniebroke/deezer-python/
    :target: https://github.com/browniebroke/deezer-python
    :alt: LoC
.. |pyversions| image:: https://img.shields.io/pypi/pyversions/deezer-python.svg?style=flat-square
.. |license| image:: https://img.shields.io/pypi/l/deezer-python.svg?style=flat-square
.. _Deezer API: http://developers.deezer.com/api
.. _API reference: https://deezer-python.readthedocs.io/api_reference/toc.html
.. _documentation: http://deezer-python.readthedocs.io/
.. _Python Social Auth: https://github.com/python-social-auth

Contents:

.. toctree::
    :maxdepth: 1

    api_reference/toc
    contributing
    changelog
    license
