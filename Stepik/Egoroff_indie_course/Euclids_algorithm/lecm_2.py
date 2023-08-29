# Наименьшее Общее Кратное 2
a, b = map(int, input().split())
c = b
d = a*b

while b > 0:
    a, b = b, a % b

print(d//a)
