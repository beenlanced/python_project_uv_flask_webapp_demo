# Methodology: Inspired by the examples provided in:
# URL: https://www.youtube.com/watch?v=zsYIw6RXjfM
# Date Accessed: May 2, 2025
# Source: Tech with Tim.
#
# URL: https://www.geeksforgeeks.org/flask-http-methods-handle-get-post-requests/
# Date Accessed: May 3, 2025
# Source: GeeksforGeeks.
import logging
from pathlib import Path

from typing import Hashable, Tuple

from flask import Blueprint, jsonify, render_template, Response, request
from src.get_data import get_data


logger = logging.getLogger(__name__)

data_dir_path =  Path(__file__).resolve().parent.parent.parent /"data"
data_dir_path = data_dir_path if data_dir_path.is_absolute() else Path(data_dir_path.resolve())
user_data_file = list(data_dir_path.glob("raw.csv", case_sensitive=False))[0]
user_data = get_data(str(user_data_file))

posts = Blueprint("posts", __name__)

@posts.route("/create-user", methods=["GET", "POST"])
def create_user() -> Tuple[Response, int]:
    """
    Route function that allows a user to post data via jason post
    to the web app:

    Examples:
        Use a tool like cURL or Postman to send POST requests to your Flask application.
        
        In Postman
        >>> Select POST; enter url: http://127.0.0.1:5000/create-user 
        >>> Choose option Body
        >>> Select raw radial button
        >>> Select JSON pull down
        >>> Enter the following JSON in the field window
            {
                "user_id": 123
            }
        >>> hit SEND

        Status: 201 Created
        body response
        {
            "user_id": 123
        }
    """
    logger.info("The /create-user route accessed")
    try:
        data = request.get_json()
    except Exception as e:
        logger.error("%s: Unable to parse data as JSON. HTTP Return code (415) - Unsupported Media Type response", e)
    return jsonify(data), 201

@posts.route("/handle-post", methods=["POST"])
def handle_post(user_data: dict[Hashable, str] = user_data) -> str:
    """
    Route function that allows a user to post data to an html form
    to the web app:
    
     Args:
        user_data(dict): contents of a CSV file rendered as a dictionary. Modeling DB entry

    Returns:
        str: html

    Raises:
        dict: the user data from this simple example

    Examples:
        Via GUI Interface (http://127.0.0.1:5000/) enter the following values for each field:
        >>> user_id: 100
        >>> name: john doe
        >>> email: john.doe@example.com
        Sorry, User already Exists.

        Via GUI Interface (http://127.0.0.1:5000/) enter the following values for each field:
        >>> user_id: 100
        >>> name: john doe
        >>> email: jane.doe@example.com
        Email is available. Welcome New User!
    """
    logger.info("The /handle-post route accessed")
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
        if user_data["name"] == name and user_data["email"] == email:
            return '<h1>Sorry, User already Exists.</h1>'
        else:
            return '<h1>Email is available. Welcome New User!</h1>'
        
    else:
        return render_template('get_post.html')