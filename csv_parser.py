import csv
from collections import Counter


class CSVParser:
    """Класс для парсинга CSV-файлов и подсчета количества вхождений ID"""

    def __init__(self, file_name):
        """Инициализирует CSVParser и парсит CSV-файл"""
        self.file_name = file_name
        self.id_counter = Counter()
        self._parse_csv()

    def _parse_csv(self):
        """Парсит CSV-файл и заполняет счетчик id_counter"""
        with open(self.file_name, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.id_counter[row['id']] += 1

    def get_ids_with_count(self, count):
        """
        Возвращает список ID, которые встречаются указанное количество раз
        """
        return [id for id, cnt in self.id_counter.items() if cnt == count]

    def get_frequency(self):
        """Возвращает распределение частоты вхождений ID"""
        return Counter(self.id_counter.values())


class CSVAnalyzer:
    """Класс для анализа данных из CSV-файла"""

    def __init__(self, parser: CSVParser):
        """Инициализирует CSVAnalyzer с заданным CSVParser"""
        self.parser = parser

    def print_results(self):
        """
        Выводит анализ данных: ID, встречающиеся 3 раза, и распределение
        частот
        """
        three_times_ids = self.parser.get_ids_with_count(3)
        all_ids_counter = self.parser.get_frequency()
        print('Частота повторений:')
        for count, ids in sorted(all_ids_counter.items()):
            print(f'{count} раз встречается {ids} id')
        print(f'ID, которые встречаются в файле 3 раза:\n{three_times_ids}')


def main():
    """Главная функция для запуска анализа CSV-файла"""
    csv_file_name = 'table.csv'
    parser = CSVParser(csv_file_name)
    analyser = CSVAnalyzer(parser)
    analyser.print_results()


if __name__ == '__main__':
    main()
