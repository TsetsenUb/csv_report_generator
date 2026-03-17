import argparse

from src.reports.report_factory import ReportFactory


class ArgsParser:
    """Класс для парсинга и валидации аргументов командной строки."""

    def __init__(self):
        self.files: list[str] | None = None
        self.report: str | None = None
        self.delimiter: str | None = None
        self.__valid_reports: list[str] = ReportFactory.get_report_names()

        self.__parse_arguments()

    def __parse_arguments(self):
        """Парсит аргументы командной строки."""

        parser = argparse.ArgumentParser(
            description="Программа для формирования отчетов по переданным csv-файлам",
        )

        parser.add_argument(
            "--files",
            nargs="*",
            required=True,
            type=str,
            help="Список csv-файлов для обработки",
        )

        parser.add_argument(
            "--report",
            type=str,
            required=True,
            choices=self.__valid_reports,
            help=f"Тип отчета. Допустимые значения: [{', '.join(self.__valid_reports)}]",
        )

        parser.add_argument(
            "--delimiter",
            default=",",
            type=str,
            help="Разделитель для чтения csv-файлов",
        )

        args = parser.parse_args()
        self.files = args.files
        self.report = args.report
        self.delimiter = args.delimiter
