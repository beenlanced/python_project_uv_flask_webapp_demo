"""
Custom Exceptions 

Used Here to show where and How we might create custom exceptions. 
Note these are merely exemplary examples.
"""


class DataIngestionError(Exception):
    """
    Base exception for all data ingestion related errors

    Attributes:
        message -- explanation of the error
    """
    default_message = "A data ingestion -related error occurred"

    def __init__(self, message: str) -> None:
        super().__init__(message or self.default_message)

    def __str__(self):
        return f"{self.message}"


class SourceDataFileEmptyError(DataIngestionError):
    """Raised when a source data file is present, but is empty. """

    def __init__(self, message: str, filename: str) -> None:
        super().__init__(message)
        self.filename = filename
        self.message = message

    def __str__(self) -> str:
        return f"{self.message} with file {self.filename})"