from typing import Hashable

import pandas as pd
from pandas.errors import EmptyDataError

from src.utils.setup_logging import logger


def get_data(file_path: str) -> dict[Hashable, str]:
    """
    Extract data from csv file and convert into dictionary

    This method takes file_name as input and will extract the
    the contents of the file and returns the contents as a dictionary.

    Args:
        file_name(str): the name of a csv file to extract data.

    Returns:
        dict: the user data from this simple example

    Raises:
        FileNotFoundError: If the file specified by file_name does not exist
        pd.errors.EmptyDataError: If the file does exist, but is empty

    Examples:
        >>> get_data(some_file_name.csv)
        {"user_id": "100", "name": "john doe", "email": john.doe@example.com}
    """
    try:
        df = pd.read_csv(file_path)
        logger.info("CSV data file was converted to a dictionary")
        return df.to_dict('records')[0]
    except FileNotFoundError as e:
        logger.error(f"Error: File not found at {file_path} - {e}", exc_info=True)
        raise
        return None
    except EmptyDataError as e:
        logger.error(f"File is empty at {file_path} - {e}", exc_info=True)
        raise
        return None
    except Exception as e:
        logger.error(f"ERROR: An unexpected error occurred: {e}", exc_info=True)
        raise
        return None