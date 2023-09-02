"""
На вход программе поступает список из целых чисел.
Ваша задача найти в данном списке наименьшее положительное значение.
В случае, если положительных значений нет, выведите строку "Empty"

Sample Input 1:
8 11 -9 0 5 -20
Sample Output 1:
5
Sample Input 2:
5 -2 -1 18 4 -6
Sample Output 2:
4
Sample Input 3:
-4 -7 0 -19
Sample Output 3:
Empty
"""

lst = list(map(int, input().split()))
num = flag = 0

for i in lst:
    if i > 0 and flag == 0:
        num = i
        flag += 1
    elif i > 0 and i < num:
        num = i

print(num if flag > 0 else 'Empty')
