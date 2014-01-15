"""Python `Deezer API <http://developers.deezer.com/api>`_ Wrapper.

The point is to implements several classes to interact with
all types of Deezer objects, do some searches, etc...

The package is not mature at all at the moment."""

__version__ = '0.1'
__all__ = ['Client', 'Resource', 'Album']

USER_AGENT = 'Deezer Python API Wrapper v%s' % __version__

from deezer.client import Client
from deezer.resources import Album
