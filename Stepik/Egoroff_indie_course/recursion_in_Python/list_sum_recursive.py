"""
Напишите функцию list_sum_recursive,
которая принимает на вход список из целых чисел
и возвращает сумму элементов переданного списка.
Не забывайте, что реализовать это нужно при помощи рекурсии.

Ваша задача только написать определение функции list_sum_recursive

Sample Input:
1 2 3
Sample Output:
6
"""


def list_sum_recursive(arr: list, summa: int = 0) -> int:
    if len(arr) == 0:
        return summa

    return list_sum_recursive(arr, summa=(summa + arr.pop()))
