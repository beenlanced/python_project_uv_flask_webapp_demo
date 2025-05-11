# Functional Tests Here Use the Pytest Framework

Functional tests are an essential part of the development of a product because they ensure that the software application satisfies the requirements or specifications. Functional tests verify that functions/methods of the software applicaton work in conformance with the requirements and specification. It is different from unit testing because functional tests are concerned about the functionality of the application. When the functionality is tested by providng the appropriate test input(s), will the outputs of the test match with expected outputs.

This section of the repository demonstrates the functional tests applied for this application using `pytest`.

## Built With

[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)

[![Pytest](https://img.shields.io/badge/pytest-8.3.5-green)](https://docs.pytest.org/en/7.1.x/)

## Running unit tests

To run all functional tests and the unit tests as well (recommended), run `pytest` in the projects root directory (i.e., the top most directory).

```bash
cd <root_directory name>
pytest
```

As many users are using UV, you can alternatively use:

```bash
cd <root_directory name>
uv run pytest -vvv
```

The `-vvv` flag in pytest provides the `highest` level of verbosity. In other words, ti provides the most detailed information about pytest results.

More details about pytest can be found here:
[pytest documentation](https://docs.pytest.org/en/stable/)

Alternatively, you can selectively test each test file or a particular unit test case of a file performing the following:

#### Test Individual Test File

To run an individual unit test file, change directories to the file where the test file exists and then at the command / terminal prompt type `pytest test_filename.py`.

```bash
cd path_where_testfle_exists
pytest test_filename.py
```

As many users are using UV, you can alternatively use

```bash
cd path_where_testfle_exists
uv run pytest -vvv test_filename.py
```

#### Test Particular Test Case of a Test File

To run a particular unit test case in a test file, change directories to the file where the test file exists and then at the command / terminal prompt type `pytest test_filename.py::testcasename`.

```bash
cd path_where_testfle_exists
pytest test_filename.py::testcasename
```

As many users are using UV, you can alternatively use

```bash
cd path_where_testfle_exists
uv run pytest -vvv test_filename.py::testcasename
```

## Project Tree (Replace the tree - final part)

    ├── Cost of Living
      ├── data
            ├── costofliving.csv
            ├── heatmap.png
            ├── histogram.png
            ├── comparision.png
      ├── src
        ├── process.py
        ├── modelbuilding
          ├── model.py
          ├── __pycache__

        ├── preprocessing
          ├── dataloading.py
          ├── plots.py
          ├── processing.py
          ├── __pycache__

      ├── tests
        ├── unit_tests
          ├── data
            ├── __pycache__
            ├── test_data
              ├── comparision.png
              ├── heatmap.png
              ├── historgram.png
              ├── sample.csv
            ├── __init__.py
            ├── test_data_loading.py
            ├── test_model.py
            ├── test_plots.py
      ├── requirements.txt
      ├── __init__.py
    ├── README.md
