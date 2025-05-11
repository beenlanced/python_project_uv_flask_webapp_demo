import json
from typing import Type

from flask import Flask
import pytest


def test_create_user(client: Type[Flask]) -> None:
    """
    GIVEN a Flask application configured for testing
    WHEN the '/create-user' page is requested (POST)
    THEN check that website can POST/load data via json post
    to the web app
    """
    response = client.post("/create-user", data=json.dumps({"user_id": 100}),content_type="application/json",)
    result = json.loads(response.data.decode())
    assert response.status_code == 201
    assert result.get("user_id") == 100


@pytest.mark.parametrize(("user_id", "name", "email", "message"), (
    (100, "john doe", "john.doe@example.com", b"Sorry, User already Exists."),
    (100, "jane doe", "john.doe@example.com", b"Email is available. Welcome New User!"),
    (100, "john doe", "jane.doe@example.com", b"Email is available. Welcome New User!"),
    (100, "jane doe", "jane.doe@example.com", b"Email is available. Welcome New User!"),
))
def test_handle_post(client: Type[Flask], user_id: int, name: str, email: str, message: bytes) -> None:
    """
    GIVEN a Flask application configured for testing
    WHEN the '/handle-post' page is requested (POST)
    THEN check that website allows a user to post data to an html form
         to the web app by checking whether name and email matches name and 
         and email from a dictionary serving as app's database
    """
    post_data = {"user_id": user_id, "name": name, "email": email}
    response = client.post("/handle-post", data=post_data)
    assert message in response.data