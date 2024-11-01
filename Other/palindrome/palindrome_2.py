"""
Палиндром

Альтернативное решение задачи.
Перебирает строку в цикле до середины строки
сравнивая символы в начале и в конце строки.
"""

import re


source = re.sub(r'[^\w\s]', '', input().lower().replace(' ', ''))
mid = int(len(source) / 2)

for i in range(mid):
    if source[i] != source[-(i+1)]:
        print('Это не полиндром!')
        break
else:
    print('Это полиндром!!!')
