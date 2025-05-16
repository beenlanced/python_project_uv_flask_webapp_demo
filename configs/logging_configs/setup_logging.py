import atexit
import json
import logging
import logging.config

from pathlib import Path



def configure_loggers() -> None:
    """
    Configure loggers for the Flask application
    """
    json_config_path =  Path(__file__).resolve().parent.parent.parent /"configs/logging_configs"
    json_config_path = json_config_path if json_config_path.is_absolute() else Path(json_config_path.resolve())
    json_config_file = list(json_config_path.glob("*.json", case_sensitive=False))[0]

    with open(json_config_file) as f:
        config = json.load(f)
    
    logging.config.dictConfig(config)
    queue_handler = logging.getHandlerByName("queue_handler")
    if queue_handler is not None:
        queue_handler.listener.start()
        atexit.register(queue_handler.listener.stop)
    
    return None
