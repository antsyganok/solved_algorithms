"""
Дано натуральное число N.
Определить, является ли оно простым.
Натуральное число N называется простым,
если у него есть только два делителя: единица и само число N.

В качестве ответа выведите "Yes", если число простое,
"No" - в противном случае.

Sample Input:
5
Sample Output:
Yes
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
if 1 < len(lst) < 3:
    print('Yes')
else:
    print('No')
