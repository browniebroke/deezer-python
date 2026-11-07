import typing

import httpx2


class DeezerQueryAuth(httpx2.Auth):
    """
    Deezer Auth for httpx2.

    Attach given access token to the request,
    by passing it as query parameter.

    :param access_token: Your Deezer access token.
    """

    def __init__(self, access_token: str):
        self.access_token = access_token

    def auth_flow(self, request: httpx2.Request) -> typing.Generator[httpx2.Request, httpx2.Response, None]:
        """
        Add authentication query parameter to the request.

        :param request: httpx2.Request
        :return: httpx2.Request
        """
        request.url = request.url.copy_merge_params({"access_token": self.access_token})
        yield request
