import pytest
from typing import Type, Iterator, Any

from src.reports.base_report import BaseReport
from src.reports.report_factory import ReportFactory
from src.reports.median_coffee_report import MedianCoffeeReport
from tests.test_reports.results import median_coffee_display, median_coffee_result


@pytest.fixture
def new_report_name() -> str:

    return "new_report"


@pytest.fixture
def new_report_class(new_report_name: str) -> Type[BaseReport]:

    class NewReport(BaseReport):

        def generate(self, data):
            pass

        def display(self, result):
            pass

    return NewReport


@pytest.fixture
def add_new_report(
    new_report_name: str,
    new_report_class: BaseReport,
) -> Iterator[None]:

    ReportFactory.register_report(new_report_name, new_report_class)

    yield

    ReportFactory._reports.pop(new_report_name)


@pytest.fixture(scope="session")
def median_coffee_report(
    median_coffee_report_name: str,
) -> MedianCoffeeReport:

    return MedianCoffeeReport(median_coffee_report_name)


@pytest.fixture(scope="session")
def median_coffee_report_result() -> list[list[Any]]:

    return median_coffee_result


@pytest.fixture
def median_coffee_report_display() -> str:
    return median_coffee_display
