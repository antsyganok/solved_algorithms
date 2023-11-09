"""
Анаграмма

Cтрока S1 называется анаграммой строки S2,
если она получается из S2 перестановкой символов.

Программа получает на вход две строки S1 и S2.
Если строка S1 является анаграммой строки S2 нужно вывести YES,
в противном случае - NO

Sample Input 1:
abc
cba
Sample Output 1:
YES
Sample Input 2:
abracadabra
cadabraabra
Sample Output 2:
YES
Sample Input 3:
abb
bbc
Sample Output 3:
NO
"""

resultado = {}
rezultat = {}
s1 = input().lower()
s2 = input().lower()

for k1, k2 in zip(s1, s2):
    if ord(k1) in range(97, 123):
        resultado[k1] = resultado.get(k1, 0) + 1
    if ord(k2) in range(97, 123):
        rezultat[k2] = rezultat.get(k2, 0) + 1

if len(s1) != len(s2):
    print('NO')
else:
    print('YES' if resultado == rezultat else 'NO')
