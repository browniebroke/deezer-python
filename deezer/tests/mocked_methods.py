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
    resource = os.path.normpath('deezer/tests/resources{}'.format(url_path))
    if os.path.isdir(resource) and not os.path.isfile("{}.json".format(resource)):
        resource = "{}/noid".format(resource)
    resource = "{}.json".format(resource)
    return open(resource, mode='rb')
