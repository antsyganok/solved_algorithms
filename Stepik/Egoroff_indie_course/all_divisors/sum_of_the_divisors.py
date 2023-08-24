"""
Программа получает на вход натуральное число N.
Нужно найти сумму его делителей.

Sample Input 1:
10
Sample Output 1:
18
Sample Input 2:
31
Sample Output 2:
32
"""
a = int(input())
i = 1
lst = []
while i*i <= a:
    if a % i == 0:
        lst.append(i)
        if i != a//i:
            lst.append(a//i)
    i += 1

print(sum(lst))
