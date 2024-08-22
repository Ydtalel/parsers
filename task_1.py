"""
Задача 1
Необходимо написать парсер CSV-файла, который в результате выполнения выведет
следующую информацию:
- id, которые встречаются в файле только 3 раза
- частота повторений (сколько уникальных ид встречалось 1 раз, 2 раза и т.д.)
"""
import csv

from collections import Counter


def parse_csv(csv_file_name):
    """
    Получает данные из csv файла возвращает объект Counter со счетчиком для
    каждого id
    """
    id_counter = Counter()

    with open(csv_file_name, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        for row in reader:
            id_counter[row['id']] += 1

    return id_counter


def main():
    """
    Подсчитывает количество id счетчик которых равен трем и выводит эти id.

    Так же подсчитывает количество id счетчик которых равен 1, 2, 3 и так
    далее, после чего выводит эту информацию.
    """
    csv_file_name = 'table.csv'
    id_counter = parse_csv(csv_file_name)
    three_times_ids = [id for id, count in id_counter.items() if count == 3]
    frequency_counter = Counter(id_counter.values())
    print('Частота повторений:')
    for count, ids in sorted(frequency_counter.items()):
        print(f'{count} раз встречается {ids} id')

    print(f'ID, которые встречаются в файле только 3 раза:\n{three_times_ids}')


if __name__ == '__main__':
    main()
