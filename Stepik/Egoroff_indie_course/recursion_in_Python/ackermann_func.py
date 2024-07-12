"""
Функция Аккермана

Описать рекурсивную функцию ackermann,
которая принимает на вход два целых числа
m и n находит значение, определенное следующим образом:

Найденное значение функция ackermann должна вернуть в качестве результата

ackermann(3, 2) => 29
ackermann(3, 0) => 5
ackermann(1, 0) => 2
ackermann(3, 5) => 253
Ваша задача только написать определение функции ackermann

В тестовых примерах сперва поступает на вход значение аргумента m,
затем аргумента n.

Sample Output 1:
7
Sample Input 2:
2
4
Sample Output 2:
11
Sample Input 3:
3
3
Sample Output 3:
61
Sample Input 4:
3
2
Sample Output 4:
29
"""


def ackermann(m: int, n: int) -> int:
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))
