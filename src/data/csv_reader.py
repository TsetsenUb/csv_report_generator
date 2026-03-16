import csv
from typing import Any


class CSVReader:
    """Класс для чтения CSV файлов"""

    def __init__(self, delimiter: str = ","):
        self.delimiter = delimiter

    def read_files(self, file_paths: list[str]) -> list[dict[str, Any]]:
        """
        Читает несколько CSV файлов и объединяет данные.
        Если при чтении файла возникла ошибка, выводит в консоль информацию об ошибке.
        """

        all_data = []

        for csv_file_path in file_paths:
            try:
                with open(csv_file_path, "r", encoding="utf-8") as f:
                    file_reader = csv.DictReader(f, delimiter=self.delimiter)

                    all_data.extend(list(file_reader))

            except Exception as er:
                print(f"[ERROR] {csv_file_path}: {er}")

        return all_data
