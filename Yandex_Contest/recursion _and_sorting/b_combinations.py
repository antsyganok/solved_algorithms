# Яндекс Контест Задача Б. "Комбинации."

kbd = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
    }


def foo(inp, buffer='', nums=0):
    if nums < len(inp):
        for letter in kbd[inp[nums]]:
            foo(inp, buffer+letter, nums+1)
    else:
        print(buffer, end=' ')


inp = input()
length = len(inp)
foo(inp)
