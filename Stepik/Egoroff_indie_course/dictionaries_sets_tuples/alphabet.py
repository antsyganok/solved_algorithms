from string import ascii_lowercase
"""
Напишите программу, которая печатает словарь alphabet,
где ключи  - строчные английские символы,
а значения - порядковые номера букв в алфавите начиная с 1.
"""

alphabet = {}

for i in ascii_lowercase:
    alphabet[i] = ord(i) - 96

print(alphabet)
