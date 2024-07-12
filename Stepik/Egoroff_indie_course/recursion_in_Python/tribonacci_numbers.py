"""
Числа Трибоначчи

Описать рекурсивную функцию tribonacci,
которая принимает на вход целое число
n - порядковый номер чисел Трибоначчи.
Функция по параметру n должна вычислить и вернуть значение,
стоящее на n-м месте в ряде чисел Трибоначчи

Вот примере вызовов:

tribonacci(0) => 0
tribonacci(2) => 1
tribonacci(4) => 2
tribonacci(6) => 7
tribonacci(7) => > 13
Ваша задача только написать определение функции tribonacci

Sample Input 1:
1
Sample Output 1:
0
Sample Input 2:
3
Sample Output 2:
1
Sample Input 3:
5
Sample Output 3:
4
Sample Input 4:
8
Sample Output 4:
24
"""


def tribonacci(n: int) -> int:
    if n < 3:
        return int(n == 2)
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)
