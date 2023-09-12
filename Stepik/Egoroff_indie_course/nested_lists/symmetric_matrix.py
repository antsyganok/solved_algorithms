"""
Симметричная ли матрица?

Проверьте, является ли двумерный массив
симметричным относительно главной диагонали.
Главная диагональ — та, которая идёт
из левого верхнего угла двумерного массива в правый нижний.

Входные данные
Программа получает на вход число n<100,
являющееся числом строк и столбцов в массиве.
Далее во входном потоке идет n строк по n чисел,
являющихся элементами массива.

Выходные данные
Программа должна выводить слово
Yes для симметричного массива и слово
No для не симметричного.

Sample Input 1:
3
0 1 2
1 5 3
2 3 4
Sample Output 1:
Yes
Sample Input 2:
3
0 0 0
0 0 0
1 0 0
Sample Output 2:
No

Sample Input 4:
5
0 1 2 3 4
1 0 5 6 7
2 5 0 8 9
3 6 8 0 8
4 7 9 8 0
Sample Output 4:
Yes
"""

break_out_flag = False
lst = []
for _ in range(n := int(input())):
    lst.append(list(map(int, input().strip().split())))

for i in range(n):
    for j in range(n):
        if i != j and lst[i][j] != lst[j][i]:
            print('No')
            break_out_flag = True
            break
    if break_out_flag:
        break
else:
    print('Yes')
