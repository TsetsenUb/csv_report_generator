from src.cli.args_parser import ArgsParser
from src.data.csv_reader import CSVReader
from src.reports.report_factory import ReportFactory


def main():

    # Получаем аргументы командной строки
    args = ArgsParser()

    # Читаем данные
    csv_reader = CSVReader(args.delimiter)
    all_data = csv_reader.read_files(args.files)

    # Генерация и вывод отчета в консоль
    report = ReportFactory.create_report(args.report)
    result = report.generate(all_data)
    report.display(result)


if __name__ == "__main__":
    main()
