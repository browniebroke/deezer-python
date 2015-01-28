try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse
import os


def fake_urlopen(url):
    """
    Get data from fs
    """
    url_path = urlparse(url).path
    resource = os.path.normpath('deezer/tests/resources%s' % url_path)
    if os.path.isdir(resource) and not os.path.isfile(resource + ".json"):
        resource += "/noid"
    resource += ".json"
    return open(resource, mode='rb')
