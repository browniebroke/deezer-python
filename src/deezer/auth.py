import typing

import httpx


class DeezerQueryAuth(httpx.Auth):
    """
    Deezer Auth for httpx.

    Attach given access token to the request,
    by passing it as query parameter.

    :param access_token: Your Deezer access token.
    """

    def __init__(self, access_token: str):
        self.access_token = access_token

    def auth_flow(self, request: httpx.Request) -> typing.Generator[httpx.Request, None, None]:
        """
        Add authentication query parameter to the request.

        :param request: httpx.Request
        :return: httpx.Request
        """
        request.url = request.url.copy_merge_params({"access_token": self.access_token})
        yield request
