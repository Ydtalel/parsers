"""
Задача 2
Необходимо написать парсер электронной книги в формате epub или fb2 (выбор за
Вами)
На входе - любой файл в виде аргумента к консольной команде.
На выходе - список "Название книги, имя автора, название издательства, год
издания"
"""

import sys
import warnings

from ebooklib import epub

warnings.filterwarnings("ignore")


def parse_epub(file):
    """
    Получает содержимое файла формата epub и извлекает и возвращает данные:
    название книги, авторы, название издательства, год издания
    """
    book = epub.read_epub(file)

    title = book.get_metadata('DC', 'title')
    authors = book.get_metadata('DC', 'creator')
    publisher = book.get_metadata('DC', 'publisher')
    date = book.get_metadata('DC', 'date')

    title = title[0][0] if title else 'Не указано'
    authors = (', '.join(author[0] for author in authors) if authors
               else 'Не указано')
    publisher = publisher[0][0] if publisher else 'Не указано'
    date = date[0][0] if date else 'Не указано'
    return title, authors, publisher, date


def main():
    """
    Считывает аргументы консольной команды и выводит информацию:
    название книги, авторы, название издательства, год издания
    """
    if len(sys.argv) < 2:
        print('Запуск: python parser.py <путь_к_файлу.epub>')
        return

    file = sys.argv[1]

    title, author, publisher, date = parse_epub(file)
    print(f'Название книги: {title}\nАвторы: {author}\nНазвание издательства: '
          f'{publisher}\nГод издания: {date}')


if __name__ == '__main__':
    main()
