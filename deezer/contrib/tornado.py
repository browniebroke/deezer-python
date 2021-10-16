"""
Implements an async tornado client class to query the
`Deezer API <http://developers.deezer.com/api>`_
"""
import json
import logging
from urllib.parse import urlencode

from tornado.gen import Return, coroutine
from tornado.httpclient import AsyncHTTPClient

from deezer.client import Client


class AsyncClient(Client):
    """
    An async client to retrieve some basic infos about Deezer resources.

    Create a client instance with the provided options. Options should
    be passed in to the constructor as kwargs.

        >>> from deezer.contrib.tornado import AsyncClient
        >>> client = AsyncClient(app_id='foo', app_secret='bar')

    This client provides several method to retrieve the content of most
    sort of Deezer objects, based on their json structure.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        max_clients = kwargs.get("max_clients", 2)
        self._async_client = AsyncHTTPClient(max_clients=max_clients)

    @coroutine
    def get_object(
        self, object_t, object_id=None, relation=None, parent=None, **kwargs
    ):
        """
        Actually query the Deezer API to retrieve the object

        :returns: json dictionary or raw string if other
                  format requested
        """
        url = self.object_url(object_t, object_id, relation, **kwargs)
        logging.debug(url)
        response = yield self._async_client.fetch(url)
        resp_str = response.body.decode("utf-8")
        jsn = json.loads(resp_str)
        result = self._process_json(jsn, parent)
        raise Return(result)

    @coroutine
    def request(self, method: str, path: str, **params):
        """
        Make a request to the API and parse the response.

        :param method: HTTP verb to use: GET, POST< DELETE, ...
        :param path: The path to make the API call to (e.g. 'artist/1234')
        :param params: Query parameters to add the the request
        """
        if self.access_token is not None:
            params["access_token"] = str(self.access_token)

        url = f"{self.base_url}/{path}"
        if params:
            url = f"{url}?{urlencode(params)}"

        response = yield self._async_client.fetch(url, method=method)
        resp_str = response.body.decode("utf-8")
        json_data = json.loads(resp_str)
        result = self._process_json(json_data)
        raise Return(result)
