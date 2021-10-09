from typing import Dict

import requests


class DeezerAPIException(Exception):
    """Base exception for API errors."""


class DeezerRetryableException(DeezerAPIException):
    """A request failing with this might work if retried."""


class DeezerHTTPError(DeezerAPIException):
    """Specialisation wrapping HTTPError from the requests library."""

    def __init__(self, http_exception: requests.HTTPError, *args: object) -> None:
        if http_exception.response is not None and http_exception.response.text:
            url = http_exception.response.request.url
            status_code = http_exception.response.status_code
            text = http_exception.response.text
            super().__init__(status_code, url, text, *args)
        else:
            super().__init__(http_exception, *args)

    @classmethod
    def from_http_error(cls, exc: requests.HTTPError) -> "DeezerHTTPError":
        if exc.response.status_code in {502, 503, 504}:
            return DeezerRetryableHTTPError(exc)
        if exc.response.status_code == 403:
            return DeezerForbiddenError(exc)
        if exc.response.status_code == 404:
            return DeezerNotFoundError(exc)
        return DeezerHTTPError(exc)


class DeezerRetryableHTTPError(DeezerRetryableException, DeezerHTTPError):
    """A HTTP error due to a potentially temporary issue."""


class DeezerForbiddenError(DeezerHTTPError):
    """A HTTP error cause by permission denied error."""


class DeezerNotFoundError(DeezerHTTPError):
    """For 404 HTTP errors."""


class DeezerErrorResponse(DeezerAPIException):
    """A functional error when the API doesn't accept the request."""

    def __init__(self, json_data: Dict[str, str]) -> None:
        self.json_data = json_data
