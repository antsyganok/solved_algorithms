# Наименьшее Общее Кратное
a, b = map(int, input().split())
c = b

while c % a > 0:
    c += b

print(c)
