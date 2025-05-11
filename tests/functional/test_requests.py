from typing import Type

from flask import Flask
import pytest


def test_get_user(client: Type[Flask]) -> None:
    """
    GIVEN a Flask application configured for testing
    WHEN the '/get-user/<user_id>' page is requested (GET)
    THEN check that the response returns a tuple of a JSON response derieved from CSV data
         plus user request data and an integer response code
    """
    response = client.get('/get-user/123?extra="hello"')
    assert response.status_code == 200
    assert response.json == {
            "email": "john.doe@example.com",
            "extra": "\"hello\"",
            "name": "john doe",
            "user_id": "123"
    }

@pytest.mark.parametrize(("user_id", "name", "email", "message"), (
    (100, "john doe", "john.doe@example.com", b"Welcome!"),
    (100, "jane doe", "john.doe@example.com", b"Invalid Credentials!"),
    (100, "john doe", "jane.doe@example.com", b"Invalid Credentials!"),
    (100, "jane doe", "jane.doe@example.com", b"Invalid Credentials!"),
))
def test_handle_get(client: Type[Flask], user_id: int, name: str, email: str, message: bytes) -> None:
    """
    GIVEN a Flask application configured for testing
    WHEN the '/handle_get' page is requested (GET)
    THEN check whether name and email matches name and email from a dictionary serving as app's database
    """
    get_data = {"user_id": user_id, "name": name, "email": email}
    get_str = f'/handle_get?user_id={get_data.get("user_id")}&name={get_data.get("name")}&email={get_data.get("email")}'
    
    response = client.get(get_str)
    assert message in response.data