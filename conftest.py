import pytest

import deezer


@pytest.fixture()
def client():
    return deezer.Client(app_id="foo", app_secret="bar")  # nosec
