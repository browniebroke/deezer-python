deezer-python
=============
|build-status| |coverage-status| |docs| |pypi| |quantified| |landscape|

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
    :target: https://readthedocs.org/projects/deezer-python/?badge=latest
    :alt: Documentation Status
.. |pypi| image:: https://badge.fury.io/py/deezer-python.svg
    :target: http://badge.fury.io/py/deezer-python
    :alt: PyPi Status
.. |quantified| image:: http://www.quantifiedcode.com/api/v1/project/de55c920c85746b793e5e3103700c7a8/badge.svg
    :target: http://www.quantifiedcode.com/app/project/de55c920c85746b793e5e3103700c7a8
    :alt: Code issues
.. |landscape| image:: https://landscape.io/github/browniebroke/deezer-python/master/landscape.svg?style=flat
   :target: https://landscape.io/github/browniebroke/deezer-python/master
   :alt: Code Health    
.. _Deezer API: http://developers.deezer.com/api
.. _Sphinx: http://sphinx-doc.org/
.. _documentation: http://deezer-python.readthedocs.org/
