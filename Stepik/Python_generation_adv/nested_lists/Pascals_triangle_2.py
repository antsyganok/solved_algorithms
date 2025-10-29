"""
Треугольник Паскаля 2

На вход программе подается натуральное число n.
Напишите программу, которая выводит первые
n строк треугольника Паскаля.

Формат входных данных
На вход программе подается число n (n≥1).

Формат выходных данных
Программа должна вывести первые n строк треугольника Паскаля,
каждую на отдельной строке в соответствии с образцом.

Sample Input 1:
4
Sample Output 1:
1
1 1
1 2 1
1 3 3 1

Sample Input 2:
5
Sample Output 2:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1

Sample Input 3:
2
Sample Output 3:
1
1 1
"""


def fctorial(x: int) -> int:
    if x == 0:
        return 1
    elif 0 < x < 3:
        return x
    else:
        return fctorial(x - 1) * x


def pascal_triangle(num: int) -> None:

    for n in range(num):
        my_list = []
        for k in range(n+1):
            my_list.append(int(fctorial(n) / (fctorial(k) * fctorial(n - k))))
        print(*my_list)


pascal_triangle(int(input()))
