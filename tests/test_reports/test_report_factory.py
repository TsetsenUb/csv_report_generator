import pytest

from src.reports.report_factory import ReportFactory
from src.reports.base_report import BaseReport


@pytest.mark.report_factory
class TestReportFactory:

    @staticmethod
    def test_register_report(
        new_report_name: str,
        new_report_class: BaseReport,
    ):
        ReportFactory.register_report(new_report_name, new_report_class)

        reports = ReportFactory._reports

        assert new_report_name in reports
        assert new_report_class is reports[new_report_name]

        reports.pop(new_report_name)

    @staticmethod
    def test_register_report_with_wrong_class(
        new_report_name: str,
    ):
        class WrongClass:
            pass

        with pytest.raises(TypeError) as excinfo:
            ReportFactory.register_report(new_report_name, WrongClass)
            assert excinfo.value == "The report_class should be a subclass of BaseReport"

    @staticmethod
    def test_report_names():
        report_names = ReportFactory.get_report_names()

        assert isinstance(report_names, list)
        assert "median-coffee" in report_names

    @staticmethod
    def test_create_report(
        new_report_name: str,
        new_report_class: BaseReport,
        add_new_report,
    ):
        obj_report = ReportFactory.create_report(new_report_name)

        assert isinstance(obj_report, new_report_class)

    @staticmethod
    def test_create_report_with_wrong_name():

        wrong_name = "wrong_name"

        with pytest.raises(ValueError) as excinfo:
            ReportFactory.create_report(wrong_name)
            assert excinfo.value == f"Unknown report type: {wrong_name}"
