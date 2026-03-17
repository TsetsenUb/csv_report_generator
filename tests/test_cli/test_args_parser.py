import pytest

from src.cli.args_parser import ArgsParser


@pytest.mark.args_parser
class TestArgsParser:

    @staticmethod
    def test_args_parser(
        file_paths: list[str],
        median_coffee_report_name: str,
        mock_parse_args,
    ):

        parser = ArgsParser()

        assert parser.files == file_paths
        assert parser.report == median_coffee_report_name
        assert parser.delimiter == ","

    @staticmethod
    def test_args_parser_no_files(
        mock_parse_args_no_files,
    ):

        with pytest.raises(AttributeError):
            ArgsParser()

    @staticmethod
    def test_args_parser_no_report(
        mock_parse_args_no_report,
    ):

        with pytest.raises(AttributeError):
            ArgsParser()
