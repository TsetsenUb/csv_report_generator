import pytest
from pytest import CaptureFixture
from typing import Any

from src.data.csv_reader import CSVReader


@pytest.mark.csv_reader
class TestCSVReader:

    @staticmethod
    def test_read_files(
        file_paths: list[str],
        all_test_data: list[dict[str, Any]],
    ):

        reader = CSVReader(delimiter=",")

        all_data = reader.read_files(file_paths)

        assert all_data == all_test_data

    @staticmethod
    def test_read_files_error(
        file_paths: list[str],
        all_test_data: list[dict[str, Any]],
        capsys: CaptureFixture,
    ):

        wrong_path = "wrong_file_path"
        paths = file_paths[:2] + [wrong_path]
        reader = CSVReader(delimiter=",")

        data = reader.read_files(paths)

        captured = capsys.readouterr()

        assert captured.out == f"[ERROR] {wrong_path}: [Errno 2] No such file or directory: '{wrong_path}'\n"
        assert data[0] in all_test_data
        assert data[-1] in all_test_data
        assert data != all_test_data
