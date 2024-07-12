"""
Ваша задача реализовать этот алгоритм.
Для этого нужно будет создать функцию quick_sort,
которая будет принимать исходный список и возвращать
новый отсортированный в порядке неубывания список.

Необходимо написать только определение функций quick_sort,
при этом нельзя пользоваться встроенными сортировками в Python

Sample Input 1:
5
19 4 5 17 1
Sample Output 1:
1 4 5 17 19
Sample Input 2:
8
16 19 2 12 20 15 20 15
Sample Output 2:
2 12 15 15 16 19 20 20
"""


def quick_sort(s):
    if len(s) <= 1:
        return s
    else:
        central = s[len(s) // 2]
        left = []
        right = []
        mid = []

        for i in s:
            if i < central:
                left.append(i)
            elif i > central:
                right.append(i)
            else:
                mid.append(i)

        return quick_sort(left) + mid + quick_sort(right)
