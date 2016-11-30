deezer-python
=============
|build| |coverage| |docs| |pypi| |quantified| |landscape|

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

Running Tests
-------------

Tests are run using `Tox`_, that you would need to have installed in
your environment. Then simply run:

::

    % tox [-e py35]
    py35 runtests: commands[0] | python -m coverage run -m unittest discover
    ................................
    ----------------------------------------------------------------------
    Ran 32 tests in 1.319s

    OK
    py35 runtests: commands[1] | python /Users/Bruno/Documents/Workspace/deezer-python/run_coveralls.py
    _____________ summary _____________
    py35: commands succeeded
    congratulations :)


Create a New Release
--------------------

This project is configured to use `bumpversion
<https://github.com/peritus/bumpversion>`_, only prerequisite
is to have it installed. When the tests have passed and you're happy with the code base, just need to run::

  $ bumpversion [major|minor|patch]

Depending on which digit of the version needs to be updated, and then push with tags::

  $ git push --tags

Travis will take care of creating the release, and upload it to PyPi.


.. |build| image:: https://travis-ci.org/browniebroke/deezer-python.svg
    :target: https://travis-ci.org/browniebroke/deezer-python
    :alt: Build status
.. |coverage| image:: https://codecov.io/gh/browniebroke/deezer-python/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/browniebroke/deezer-python
    :alt: Test coverage percentage
.. |docs| image:: https://readthedocs.org/projects/deezer-python/badge/?version=latest
    :target: https://readthedocs.org/projects/deezer-python/?badge=latest
    :alt: Documentation Status
.. |pypi| image:: https://badge.fury.io/py/deezer-python.svg
    :target: http://badge.fury.io/py/deezer-python
    :alt: PyPi Status
.. |landscape| image:: https://landscape.io/github/browniebroke/deezer-python/master/landscape.svg?style=flat
   :target: https://landscape.io/github/browniebroke/deezer-python/master
   :alt: Code Health    
.. _Deezer API: http://developers.deezer.com/api
.. _Sphinx: http://sphinx-doc.org/
.. _documentation: http://deezer-python.readthedocs.org/
.. _Tox: http://tox.readthedocs.io/en/stable/index.html
.. _Python Social Auth: https://github.com/omab/python-social-auth
