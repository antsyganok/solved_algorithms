"""
Палиндром
"""

import re


source = re.sub(r'[^\w\s]', '', input().lower().replace(' ', ''))
mid = int(len(source) / 2)

print('Палиндром!!!' if source[:mid] == source[:mid:-1] else 'Не палиндром!')
