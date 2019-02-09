# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

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
    mkpath("album", "302127", "tracks0"): "album/302127/tracks?index=0",
    mkpath("album", "302127", "tracks14"): "album/302127/tracks?index=14",
    mkpath("genre", "noid"): "genre",
    mkpath("radio", "noid"): "radio",
    mkpath("search", "noid"): "search/track?q=Billy+Jean",
    mkpath("search", "noid-noqs"): "search?q=Billy+Jean",
    mkpath("search_1", "noid"): "search?q=Billy Jean&limit=2&index=2",
    mkpath("advanced_search", "simple"): 'search?q=artist:"Lou Doillon"',
    mkpath(
        "advanced_search", "complex"
    ): 'search?q=artist:"Lou Doillon" album:"Lay Low"',
    mkpath(
        "advanced_search", "with_relation"
    ): "search/track?q=artist%3A%22Lou+Doillon%22+track%3A%22Joke%22",
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
            cls.requests_mocker.get(url, json=data, complete_qs=True)

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
