import logging

from flask import Blueprint, render_template


logger = logging.getLogger(__name__)

home_page = Blueprint("home_page", __name__)

@home_page.route("/", methods=["GET"])
def view_form() -> str:
    """
    Route function that returns either a string or status code
    """
    logger.info("The / route accessed")
    return render_template("get_post.html")

@home_page.route("/home", methods=["GET"])
def home() -> str:
    """
    Route function that returns either a string or status code
    """
    logger.info("The /home route accessed")
    return render_template("home.html")

@home_page.route("/favicon.ico", methods=["GET"])
def favicon() -> str:
    """
    Route function that handles the favion.ico search performed by most browsers.
    Put here to remove the INFO return code 404 tag that FLASK wilfrom the logs
    """
    logger.info("The /favicon.ico route accessed")
    return "No Favicon - Ignore log message produced here"