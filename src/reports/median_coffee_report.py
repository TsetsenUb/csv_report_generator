from src.reports.base_report import BaseReport
from collections import defaultdict
from typing import Any
from tabulate import tabulate
import statistics


class MedianCoffeeReport(BaseReport):
    """Отчёт о медианных тратах на кофе по студентам."""

    @property
    def name(self) -> str:
        """Геттер для имени отчета."""

        return "median-coffee"

    def __group_by_student(self, data: list[dict[str, Any]]) -> dict[str, list[int]]:
        """
        Группирует данные о тратах на кофе по студентам.

        Проходит по всем записям, извлекает имя студента и сумму трат,
        фильтрует только валидные числовые значения и собирает их в список
        для каждого студента.
        """

        result = defaultdict(list)

        for row in data:
            student: str | None = row.get("student")
            coffee_spent: str | None = row.get("coffee_spent")

            if student and coffee_spent and coffee_spent.isdigit():
                result[student].append(int(coffee_spent))

        return dict(result)

    def __calculate_medians(self, students_data: defaultdict[str, list[int]]) -> list[list]:
        """
        Для каждого студента рассчитывает медиану из списка его трат.
        """

        result = []

        for student, lst_coffee_spent in students_data.items():
            median = statistics.median(lst_coffee_spent)
            result.append([student, median])

        return result

    def generate(self, data: list[dict[str, Any]]) -> list[list[Any]]:
        """
        Вычисляет медианные траты на кофе для каждого студента.
        Возвращает отсортированный по убыванию медианных трат список [студент, медианное_значение]
        """

        students_data = self.__group_by_student(data)
        result = self.__calculate_medians(students_data)

        result.sort(key=lambda x: x[1], reverse=True)

        return result

    def display(self, result: list[list[Any]]):
        print()
        print(tabulate(result, headers=["student", self.name], tablefmt="grid"))
