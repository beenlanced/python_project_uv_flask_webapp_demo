import os
from typing import Type

from dotenv import load_dotenv
from flask import Flask

from configs.app_config import DevelopmentConfig
from src.home_page.routes import home_page
from src.posts.routes import posts
from src.requests.routes import requests
from src.utils.setup_logging import setup_logging, logger

#Load environment varables from the .env file (if present)
load_dotenv()
logger.info(f"Retrieved environmental variable: {os.environ.get("EXAMPLE_ENVIRONMENT_VARIABLE")} from .env file")

def create_app(config_class: Type[DevelopmentConfig] = DevelopmentConfig) -> Flask:
    """
    Create a configured Flask application object.

    Args:
        config_class (Type[DevelopmentConfig]): User defined subclass, DevelopmentConfig of 
            Configuration class containing app configuration. Default value set to DevelopmentConfig.

    Returns:
        (Flask): the created flask application instance configuration which has been configured by attributes in DevelopmentConfig

    Example:
        >>> app = create_app()
    """
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(home_page)
    app.register_blueprint(posts)
    app.register_blueprint(requests)

    #Set up logging
    setup_logging(app)
    return app

app = create_app()
logger.info("Flask application instance created")

if __name__ == "__main__":
    app.run(debug=True)