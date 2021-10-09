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


@pytest.fixture(scope="module", autouse=True)
def vcr_config():
    return {
        "filter_query_parameters": [("access_token", "dummy")],
    }
