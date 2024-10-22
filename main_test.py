"""Test of flask app."""
import pytest
from flask import Flask

@pytest.fixture
def app() -> Flask:
    """Create and configure a new app instance for each test."""
    from main import app
    return app

def test_hello_world(app: Flask) -> None:
    """Test the hello_world route."""
    with app.test_client() as client:
        response = client.get('/')
        assert response.data == b'Hello World!'
