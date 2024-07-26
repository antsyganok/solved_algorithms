"""
Программе на вход поступают слова,
разделенные пробелом. Ваша задача проверить,
во всех ли словах есть английская буква A
вне зависимости от регистра.
В качестве ответа программа должна вывести True или False.

Sample Input 1:
chase enlarge referee cup offense
Sample Output 1:
False
Sample Input 2:
acquaintance disAgree
Sample Output 2:
True
"""


def alla(mylst: str) -> bool:
    return all(['a' in word.lower() for word in mylst])


print(alla(list(map(str, input().split()))))
