"""Python Soundcloud API Wrapper."""

__version__ = '0.1'
__all__ = ['Client']

USER_AGENT = 'Deezer Python API Wrapper v%s' % __version__

from deezer.client import Client
