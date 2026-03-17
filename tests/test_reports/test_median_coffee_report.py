import pytest
from typing import Any
from pytest import CaptureFixture

from src.reports.median_coffee_report import MedianCoffeeReport


@pytest.mark.median_coffee
class TestMedianCoffeeReport:

    @staticmethod
    def test_name(
        median_coffee_report_name: str,
        median_coffee_report: MedianCoffeeReport,
    ):
        report_name = median_coffee_report.name

        assert report_name == median_coffee_report_name

    @staticmethod
    def test_generate(
        median_coffee_report: MedianCoffeeReport,
        all_test_data: list[dict[str, Any]],
        median_coffee_report_result: list[list[Any]],
    ):

        result = median_coffee_report.generate(all_test_data)

        assert isinstance(result, list)
        assert result == median_coffee_report_result

    @staticmethod
    def test_display(
        median_coffee_report: MedianCoffeeReport,
        median_coffee_report_result: list[list[Any]],
        median_coffee_report_display: str,
        capsys: CaptureFixture,
    ):
        median_coffee_report.display(median_coffee_report_result)

        captured = capsys.readouterr()

        assert median_coffee_report_display == captured.out
