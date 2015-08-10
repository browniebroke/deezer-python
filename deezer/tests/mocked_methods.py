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
    resource = os.path.normpath('deezer/tests/resources{0}'.format(url_path))
    if os.path.isdir(resource) and not os.path.isfile("{0}.json".format(resource)):
        resource = "{0}/noid".format(resource)
    resource = "{0}.json".format(resource)
    return open(resource, mode='rb')
