"""
Разбиение на чанки

На вход программе подаются две строки:
на одной – символы, на другой – число n.
Из первой строки формируется список.

Реализуйте функцию chunked(),
которая принимает на вход список и число,
задающее размер чанка (куска),
а возвращает список из чанков (кусков) указанной длины.

Формат входных данных
На вход программе подается строка текста, содержащая символы,
отделенные символом пробела и число n на отдельной строке.

Формат выходных данных
Программа должна вывести указанный вложенный список.

Примечание. Не забудьте вызвать функцию chunked(), чтобы вывести результат.

Sample Input 1:
a b c d e f
2
Sample Output 1:
[['a', 'b'], ['c', 'd'], ['e', 'f']]
Sample Input 2:
a b c d e f
3
Sample Output 2:
[['a', 'b', 'c'], ['d', 'e', 'f']]
Sample Input 3:
a b c d e f
6
Sample Output 3:
[['a', 'b', 'c', 'd', 'e', 'f']]
Sample Input 4:
a b c d e f r g b
2
Sample Output 4:
[['a', 'b'], ['c', 'd'], ['e', 'f'], ['r', 'g'], ['b']]
Sample Input 5:
a b
3
Sample Output 5:
[['a', 'b']]
"""


def chunked(strg: list, num: int) -> list:
    res = []
    for i in range(0, len(strg), num):
        res.append(strg[i: i + num])

    return res


print(chunked(input().split(), int(input())))
