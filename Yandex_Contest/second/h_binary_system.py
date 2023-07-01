# Яндекс Контест Задача H. "Двоичная система."

a = [*map(int, input())]
b = [*map(int, input())]

a = a[::-1]
b = b[::-1]

zeros = max(len(a), len(b))
a += [0] * (zeros - len(a))
b += [0] * (zeros - len(b))

tmp = 0
result = ''
for i in zip(a, b):
    value = i[0] + i[1] + tmp
    tmp = value // 2
    result += str(value % 2)
if tmp == 1:
    result += '1'

print(''.join(result[::-1]))
