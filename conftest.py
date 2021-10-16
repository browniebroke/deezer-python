import pytest
from environs import Env

import deezer

env = Env()
env.read_env()


@pytest.fixture()
def client():
    return deezer.Client(  # nosec
        app_id="foo",
        app_secret="bar",
        # This is to get human readable response output in VCR cassettes
        headers={"Accept-Encoding": "identity"},
    )


@pytest.fixture()
def client_token(client):
    client.access_token = env("API_TOKEN", "dummy")
    return client


def clean_response(response):
    """Remove a few info from the response before writing cassettes."""
    if not isinstance(response, dict):
        return response
    response["headers"].pop("Set-Cookie", None)
    response["headers"].pop("Date", None)
    response["headers"].pop("P3P", None)
    return response


@pytest.fixture(scope="module", autouse=True)
def vcr_config():
    return {
        "filter_query_parameters": [("access_token", "dummy")],
        "before_record_response": clean_response,
    }
