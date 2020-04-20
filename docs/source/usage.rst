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

.. _Python Social Auth: https://github.com/python-social-auth
