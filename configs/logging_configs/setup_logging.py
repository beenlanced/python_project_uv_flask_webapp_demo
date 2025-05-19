import atexit
import json
import logging
import logging.config
import os

from pathlib import Path


def configure_loggers() -> None:
    """
    Configure loggers for the Flask application
    """
    #Get json logger configuration file 
    app_base_path = str(Path(__file__).resolve().parent.parent.parent)
    json_config_file = os.path.join(app_base_path, "configs/logging_configs/logger_configure.json")

    with open(json_config_file) as f:
        config = json.load(f)

    #get absolute path for log directory and .jsonl file
    config['handlers']['file_json']['filename'] = os.path.join(app_base_path, config['handlers']['file_json']['filename'])

    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)
    
    return None
