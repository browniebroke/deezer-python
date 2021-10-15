import pytest
import requests

from deezer.exceptions import (
    DeezerForbiddenError,
    DeezerHTTPError,
    DeezerNotFoundError,
    DeezerRetryableHTTPError,
)


@pytest.mark.parametrize(
    ("status_code", "expected_exception"),
    [
        (403, DeezerForbiddenError),
        (404, DeezerNotFoundError),
        (418, DeezerHTTPError),
        (502, DeezerRetryableHTTPError),
    ],
)
def test_deezer_http_error(status_code, expected_exception):
    response = requests.Response()
    response.status_code = status_code
    http_error = requests.HTTPError(response=response)

    exc = DeezerHTTPError.from_http_error(http_error)
    assert isinstance(exc, expected_exception)
