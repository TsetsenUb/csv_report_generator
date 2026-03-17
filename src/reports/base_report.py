from abc import ABC, abstractmethod
from typing import Any


class BaseReport(ABC):
    """Базовый класс для всех отчётов."""

    def __init__(self, name):
        self._name = name

    @property
    def name(self) -> str:
        """Имя отчёта для идентификации в CLI."""
        return self._name

    @abstractmethod
    def generate(self, data: list[dict[str, Any]]) -> Any:
        """Генерирует отчёт на основе данных."""
        pass

    @abstractmethod
    def display(self, result: list[list[Any]]) -> None:
        """Отображает результат отчёта в консоли."""
        pass
