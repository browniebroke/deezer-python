try:
    from urlparse import urlparse
except ImportError:
    from urllib.parse import urlparse
import os


def fake_urlopen(url):
    """
    Get data from fs
    """
    parsed_url = urlparse(url)
    index = get_index_query(parsed_url.query)
    resource = os.path.normpath('deezer/tests/resources{0}{1}'.format(parsed_url.path, index))
    if os.path.isdir(resource) and not os.path.isfile("{0}.json".format(resource)):
        resource = "{0}/noid".format(resource)
    resource = "{0}.json".format(resource)
    return open(resource, mode='rb')


def get_index_query(query):
    """Extract the value of the index query parameter"""
    for frag in query.split('&'):
        param_frag = frag.split('=')
        if param_frag[0] == 'index' and param_frag[1] != '0':
            return param_frag[1]
    return ''
