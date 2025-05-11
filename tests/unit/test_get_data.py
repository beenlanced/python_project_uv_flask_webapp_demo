from pathlib import Path

from pandas.errors import EmptyDataError
import pytest

from src.get_data import get_data


data_dir_path =  Path(__file__).resolve().parent /"test_data"

test_data = [
    ("file_not_found", FileNotFoundError),
    ("~/path_to_file_not_found", FileNotFoundError),
]

@pytest.mark.parametrize("data_path, expected", test_data)
def test_file_not_found(data_path: str, expected: Exception) -> None:
    """
    GIVEN get_data(), a method to extract csv data
    WHEN a file path is provided
    THEN check when path to the to file does not exist or the file name
         does not exist (i.e., yields fileNotFoundError)
    """
    with pytest.raises(FileNotFoundError) as E:
        get_data(data_path)
        assert E  == expected

def test_file_is_empty() -> None:
    """
    GIVEN get_data(), a method to extract csv data
    WHEN a file path is provided and the data file exists
    THEN check that the data file empty
    """
    with pytest.raises(EmptyDataError) as E:
        empty_data_file =  str(list(data_dir_path.glob("empty.csv", case_sensitive=False))[0])
        get_data(empty_data_file)
        assert E  == EmptyDataError

def test_dictionary_obtained() -> None: # type: ignore
    """
    GIVEN get_data(), a method to extract csv data
    WHEN a file path is provided and the data file exists
    THEN check that the csv data file gets extacted to yield a dictionary
    """
    non_empty_data_file =  str(list(data_dir_path.glob("non_empty.csv", case_sensitive=False))[0])
    result_dict = get_data(non_empty_data_file)
    assert result_dict != {}