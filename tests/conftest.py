import pytest
import csv
from typing import Any


@pytest.fixture(scope="session")
def file_paths() -> list[str]:
    return [
        "tests/csv_files/math.csv",
        "tests/csv_files/physics.csv",
        "tests/csv_files/programming.csv"
    ]


@pytest.fixture(scope="session")
def all_test_data(file_paths: list[str]) -> list[dict[str, Any]]:

    all_data = []

    for file_path in file_paths:
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f, delimiter=",")
            all_data.extend(list(reader))

    return all_data


@pytest.fixture(scope="session")
def median_coffee_report_name() -> str:

    return "median-coffee"
