# Яндекс Контест Задача F. "Палиндром."

line = input()


def is_a_palindrome(line):
    line = list(filter(str.isalpha, line.lower()))
    if line == line[::-1]:
        return print(True)
    else:
        return print(False)


is_a_palindrome(line)
