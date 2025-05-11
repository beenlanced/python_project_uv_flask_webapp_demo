from typing import Generator 

from flask import Flask
from flask.testing import FlaskClient
import pytest

from src.app import create_app

@pytest.fixture
def app() -> Generator[Flask, None, None]:
    """ Create and configure a new Flask app instance for each test"""
    app = create_app()
    app.config["TESTING"] = True
    with app.app_context():
        yield app

@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """Create a Flask test client using the application fixture."""
    return app.test_client()