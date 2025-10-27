"""
Магический квадрат (H)
Магическим квадратом порядка
n называется квадратная таблица размера nxn,
составленная из всех чисел 1,2,3, …, n^2 так,
что суммы по каждому столбцу, каждой строке и
каждой из двух диагоналей равны между собой.
Напишите программу, которая проверяет,
является ли заданная квадратная матрица магическим квадратом.

Формат входных данных
На вход программе подается натуральное число n – количество строк
и столбцов в матрице, затем элементы матрицы: n строк,
по n чисел в каждой, разделенные пробелами.

Формат выходных данных
Программа должна вывести YES, если матрица является магическим квадратом,
или NO в противном случае.

Тестовые данные:
Sample Input 1:
3
8 1 6
3 5 7
4 9 2
Sample Output 1:
YES

Sample Input 2:
3
8 2 6
3 5 7
4 9 1
Sample Output 2:
NO

Sample Input 3:
3
4 9 2
3 5 7
8 1 6
Sample Output 3:
YES
"""

n = int(input())
seen = set()
col_sums = [0] * n
main_diag = 0
secondary_diag = 0
magic_sum = n * (n*n + 1) // 2

for i in range(n):
    lst = list(map(int, input().split()))

    if magic_sum != sum(lst):
        break

    for j in range(n):
        num = lst[j]

        if num == 0 or num in seen:
            print('NO')
            exit()
        seen.add(num)

        col_sums[j] += num

        if i == j:
            main_diag += num
        if i + j == n - 1:
            secondary_diag += num

if (
    main_diag == magic_sum and secondary_diag == magic_sum and
        all(s == magic_sum for s in col_sums)):
    print('YES')
else:
    print('NO')
