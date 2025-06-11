import os
import entrypoint


def test_api_connection_unauthorized(httpx_mock, monkeypatch):
    monkeypatch.setenv("LODGIFY_API_KEY", "dummy")
    httpx_mock.add_response(
        url="https://api.lodgify.com/v2/properties?limit=1",
        status_code=entrypoint.HTTP_UNAUTHORIZED,
    )
    assert entrypoint.test_api_connection() is False
