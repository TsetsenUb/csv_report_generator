from typing import Type

from src.reports import BaseReport, MedianCoffeeReport


class ReportFactory:
    """Фабрика для создания отчётов."""

    _reports: dict[str, Type[BaseReport]] = {}

    @classmethod
    def register_report(
        cls,
        name: str,
        report_class: Type[BaseReport],
    ) -> None:
        """Регистрирует новый тип отчёта."""

        cls._reports[name] = report_class

    @classmethod
    def get_report_names(cls) -> list[str]:
        """Возвращает список доступных отчётов."""

        return list(cls._reports.keys())

    @classmethod
    def create_report(cls, name: str) -> BaseReport:
        """Создаёт экземпляр объект BaseReport по имени и возвращает его."""

        report_class = cls._reports.get(name)

        if not report_class:
            raise ValueError(f"Unknown report type: {name}")

        return report_class(name)


ReportFactory.register_report("median-coffee", MedianCoffeeReport)
