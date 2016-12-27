"""Python `Deezer API <http://developers.deezer.com/api>`_ Wrapper.

Implements several classes to interact with all types of Deezer objects,
do some searches, and build application written in Python on top of it

"""
from deezer.async import AsyncClient
from deezer.client import Client
from deezer.resources import Album, Resource, Artist, Playlist
from deezer.resources import Genre, Track, User, Comment, Radio


__version__ = '0.6.0'
__all__ = ['AsyncClient', 'Client', 'Resource', 'Album',
           'Artist', 'Genre', 'Playlist', 'Track', 'User',
           'Comment', 'Radio']

USER_AGENT = 'Deezer Python API Wrapper v{0}'.format(__version__)
