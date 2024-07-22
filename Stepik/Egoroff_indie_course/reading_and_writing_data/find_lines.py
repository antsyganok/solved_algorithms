"""
Напишите функцию find_lines_len_more_6,
которая принимает имя файла и находит количество строк,
превышающее 6 символов.
Не забывайте исключать знак переноса на новую строку,
стоящий в конце строки.

Функция find_lines_len_more_6 должна возвращать
найденное количество строк

Ваша задача написать
только определение функции find_lines_len_more_6
"""

from string import punctuation


def find_lines_len_more_6(file_name: str) -> int:
    count = 0
    with open(file_name, 'r') as file:
        for word in file.read().splitlines():
            word = word.strip(punctuation)
            if len(word) > 6:
                count += 1

    return count
