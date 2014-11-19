try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse
import os

def fake_urlopen(url):
    parsed_url = urlparse(url)
    resource_file = os.path.normpath('deezer/tests/resources%s' % parsed_url.path)
    if os.path.isdir(resource_file):
        resource_file += "/noid"
    resource_file += ".json"
    return open(resource_file, mode='rb')
