# Methodology: Inspired by example provided in:
# URL: https://www.youtube.com/watch?v=zsYIw6RXjfM
# Date Accessed: May 2, 2025
# Source: Tech with Tim.
# https://flask.palletsprojects.com/en/stable/tutorial/tests/
import logging
from pathlib import Path
from typing import Hashable, Tuple

from flask import Blueprint, jsonify, render_template, Response,request
from src.get_data import get_data


logger = logging.getLogger(__name__)

data_dir_path =  Path(__file__).resolve().parent.parent.parent /"data"
data_dir_path = data_dir_path if data_dir_path.is_absolute() else Path(data_dir_path.resolve())
user_data_file = list(data_dir_path.glob("raw.csv", case_sensitive=False))[0]
user_data = get_data(str(user_data_file))

requests = Blueprint("requests", __name__)

@requests.route("/get-user/<user_id>", methods=["GET"])
def get_user(user_id: str, user_data: dict[Hashable, str] = user_data) -> Tuple[Response, int]:
    """
    Route function that returns a tuple of a JSON response derieved from CSV data
    plus user request data and an integer response code
    127.0.0.1:5000/get-user/123?extra="hello"

    Args:
        user_data(dict): contents of a CSV file rendered as a dictionary. Modeling DB entry

    Returns:
        str: html

    Examples:
        In browser window type:
        >>> http://127.0.0.1:5000/get-user/123?extra="hello"
        {
            "email": " john.doe@example.com",
            "extra": "\"hello\"",
            "name": "john doe",
            "user_id": "123"
        }
    """
    logger.info("The /get-user/<user_id> route accessed")
    user_data["user_id"] = user_id
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra
    return jsonify(user_data), 200

@requests.route('/handle_get', methods=['GET'])
def handle_get(user_data: dict[Hashable, str] = user_data) -> str:
    """
    Route function that performs GET request using forms.
    Checks if given email matches email from a dictionary.
    Typically, we would use a database, but for this demo app
    we are using a dictionary.

    Args:
        user_data(dict): contents of a CSV file rendered as a dictionary. Modeling DB entry

    Returns:
        str: html

    Examples:
        In browser window type:
        >>> http://127.0.0.1:5000/handle_get?user_id=100&name="john doe"&email=john.doe@example.com
        Welcome!

        In browser window type:
        >>> http://127.0.0.1:5000/handle_get?user_id=100&name="john doe"&email=jane.doe@example.com
        Invalid credentials!

        Via GUI Interface (http://127.0.0.1:5000/) enter the following values for each field:
        >>> user_id: 100
        >>> name: john doe
        >>> email: john.doe@example.com
        Welcome!

        Via GUI Interface (http://127.0.0.1:5000/) enter the following values for each field:
        >>> user_id: 100
        >>> name: john doe
        >>> email: jane.doe@example.com
        Invalid credentials!
    """
    logger.info("The /handle_get route accessed")
    if request.method == 'GET':
        name = request.args.get('name')
        email = request.args.get('email')
        
        if user_data["name"] == name and user_data["email"] == email:
            return '<h1>Welcome!</h1>'
        else:
            return '<h1>Invalid Credentials!</h1>'
    else:
        return render_template('get_post.html')