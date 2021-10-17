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
    remove_headers = {"Set-Cookie", "Date", "P3P"}
    if isinstance(response["headers"], dict):
        # Normal client stores headers as dict
        for header_name in remove_headers:
            response["headers"].pop(header_name, None)
    elif isinstance(response["headers"], list):
        # Tornado client stores headers as a list of 2-tuples
        response["headers"] = [
            (name, value)
            for name, value in response["headers"]
            if name not in remove_headers
        ]
    return response


@pytest.fixture(scope="module", autouse=True)
def vcr_config():
    return {
        "filter_query_parameters": [("access_token", "dummy")],
        "before_record_response": clean_response,
    }
