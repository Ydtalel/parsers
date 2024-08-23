import sys
import warnings
from ebooklib import epub

warnings.filterwarnings("ignore")


class EpubParser:
    """Класс для парсинга файлов формата EPUB и извлечения данных"""

    def __init__(self, file_name):
        """ Инициализирует EpubParser и загружает книгу"""
        self.file_name = file_name
        self.book = epub.read_epub(file_name)
        self.data = {
            'title': self._get_data('DC', 'title'),
            'authors': self._get_data('DC', 'creator', join=True),
            'publisher': self._get_data('DC', 'publisher'),
            'date': self._get_data('DC', 'date')
        }

    def _get_data(self, namespace, name, join=False):
        """Извлекает данные из книги"""
        data = self.book.get_metadata(namespace, name)
        if not data:
            return 'Не указано'
        if join:
            return ', '.join(item[0] for item in data)
        return data[0][0]

    def get_data(self):
        """Возвращает данные книги"""
        return self.data


class EbookAnalyser:
    """Класс для анализа и вывода данных электронной книги"""

    def __init__(self, parser: EpubParser):
        """Инициализирует EbookAnalyser с заданным EpubParser"""
        self.parser = parser

    def print_data(self):
        """
        Выводит данные книги: название, авторы, издательство и год издания
        """
        data = self.parser.get_data()
        print(f"Название книги: {data['title']}\nАвторы: "
              f"{data['authors']}\nНазвание издательства: "
              f"{data['publisher']}\nГод издания: {data['date']}")


def main():
    """ Главная функция для запуска анализа электронной книги"""
    if len(sys.argv) < 2:
        print('Запуск: python parser.py <путь_к_файлу.epub>')
        return

    file_name = sys.argv[1]
    parser = EpubParser(file_name)
    analyser = EbookAnalyser(parser)
    analyser.print_data()


if __name__ == '__main__':
    main()
