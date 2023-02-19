import pytest
from app import app


def test_request_example():
    with app.test_client() as client:
        response = client.get("/")
        assert b"<p>Sample Flask Application</p>" in response.data