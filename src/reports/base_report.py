from abc import ABC, abstractmethod
from typing import Any


class BaseReport(ABC):
    """Базовый класс для всех отчётов."""

    @property
    @abstractmethod
    def name(self) -> str:
        """Имя отчёта для идентификации в CLI."""
        pass

    @abstractmethod
    def generate(self, data: list[dict[str, Any]]) -> Any:
        """Генерирует отчёт на основе данных."""
        pass

    @abstractmethod
    def display(self, result: list[list[Any]]) -> None:
        """Отображает результат отчёта в консоли."""
        pass
