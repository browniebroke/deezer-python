import pytest

import deezer


@pytest.fixture()
def client():
    return deezer.Client(  # nosec
        app_id="foo",
        app_secret="bar",
        # This is to get human readable response output in VCR cassettes
        headers={"Accept-Encoding": "identity"},
    )
