from flask import Flask


def test_logging_configuration(client: Flask) -> None:
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that logs are being written to
    """
    assert "flask_app_logger" in open("logs/flask_app_log.jsonl").read()

def test_landing_page(client: Flask) -> None:
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response contains title tag "Handling of Get and Post Requests"
    """
    response = client.get('/')
    assert b"<title>Handling of Get and Post Requests</title>" in response.data


def test_home_page(client: Flask) -> None:
    """
    GIVEN a Flask application configured for testing
    WHEN the '/home' page is requested (GET)
    THEN check that the response contains title tag "HOME"
    """
    response = client.get('/home')
    assert b"<title>HOME</title>" in response.data

def test_flavicon_page(client: Flask) -> None:
    """
    GIVEN a Flask application configured for testing
    WHEN the '/favicon.ico' page is requested (GET)
    THEN check that the response contains title tag "HOME"
    """
    response = client.get('/favicon.ico')
    assert b"No Favicon - Ignore log message produced here" in response.data
    assert b"No Favicon - Ignore log message produced here" in response.get_data()