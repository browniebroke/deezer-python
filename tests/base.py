# -*- coding: utf-8
import fnmatch
import json
import os
import unittest
from os.path import join as mkpath, dirname, abspath

import requests_mock
from six.moves.urllib.parse import urljoin

HOST_ROOT = "https://api.deezer.com/"
RESOURCES_ROOT = mkpath(abspath(dirname(__file__)), "resources")
FILE_EXT = ".json"

# Override a local path -> URL path
PATH_OVERRIDES = {
    mkpath("album", "302127", "tracks14"): "album/302127/tracks?index=14",
    mkpath("genre", "noid"): "genre",
    mkpath("radio", "noid"): "radio",
}


def find_files():
    """
    Simple recursive glob for Python 2, `glob.glob`doesn't
    support recursive argument in Python 2.
    """
    files_regex = "*" + FILE_EXT
    for root, dirnames, filenames in os.walk(RESOURCES_ROOT):
        for filename in fnmatch.filter(filenames, files_regex):
            yield mkpath(root, filename)


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.requests_mocker = requests_mock.mock()
        cls.requests_mocker.start()
        for file_path in find_files():
            url = url_from_path(file_path)
            data = read_resource(file_path)
            cls.requests_mocker.get(url, json=data)

    @classmethod
    def tearDownClass(cls):
        cls.requests_mocker.stop()


def read_resource(path):
    """
    Read a json file at `path` and return it as native Python
    """
    with open(path) as fd:
        content = fd.read()
    return json.loads(content)


def url_from_path(path):
    """
    Generate a URL to be mocked from the given local file `path`

    By default, assume the same URL path as the local one,
    relatively from the `RESOURCES_ROOT` and by stripping
    the '.json' suffix. Anything less obvious should be added
    as explicit override in the `PATH_OVERRIDES` dictionary.
    """
    http_path = path[(len(RESOURCES_ROOT) + 1) : -len(FILE_EXT)]
    try:
        url_part = PATH_OVERRIDES[http_path]
    except KeyError:
        url_part = http_path.replace("\\", "/")
    return urljoin(HOST_ROOT, url_part)


class RequestsMock(requests_mock.Mocker):
    def __init__(self, *names):
        super().__init__()

        # Configure the Mocker with the content of resource path
        path = mkpath(*names) + FILE_EXT
        full_path = os.path.join(RESOURCES_ROOT, path)
        with open(full_path) as f:
            self.get(requests_mock.ANY, text=f.read())


def mocker(*names):
    """Decorator to run the function inside a RequestsMock context."""

    def decorated(func):
        def wrapper(*args, **kwargs):
            with RequestsMock(*names):
                return func(*args, **kwargs)

        return wrapper

    return decorated
