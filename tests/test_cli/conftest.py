import pytest
from argparse import Namespace
from pytest_mock import MockerFixture


@pytest.fixture
def mock_parse_args(
    file_paths: list[str],
    median_coffee_report_name: str,
    mocker: MockerFixture,
) -> None:

    mock_parse = mocker.patch("argparse.ArgumentParser.parse_args")
    mock_parse.return_value = Namespace(
        files=file_paths,
        report=median_coffee_report_name,
        delimiter=",",
    )


@pytest.fixture
def mock_parse_args_no_files(
    median_coffee_report_name: str,
    mocker: MockerFixture,
) -> None:

    mock_parse = mocker.patch("argparse.ArgumentParser.parse_args")
    mock_parse.return_value = Namespace(
        report=median_coffee_report_name,
        delimiter=",",
    )


@pytest.fixture
def mock_parse_args_no_report(
    file_paths: list[str],
    mocker: MockerFixture,
) -> None:

    mock_parse = mocker.patch("argparse.ArgumentParser.parse_args")
    mock_parse.return_value = Namespace(
        files=file_paths,
        delimiter=",",
    )
