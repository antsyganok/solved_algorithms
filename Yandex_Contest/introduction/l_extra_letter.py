# Яндекс Контест Задача L. "Лишняя буква."

s = input()
t = input()


for index in range(len(t)):
    symbol = t[index]
    if symbol in s:
        s = s.replace(symbol, '', 1)
    else:
        print(symbol)
