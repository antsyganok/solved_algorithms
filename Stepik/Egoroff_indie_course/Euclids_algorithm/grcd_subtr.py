# Наибольший Общий Делитель методом вычитания
a, b = map(int, input().split())

while a != b:
    if a>b:
        a -= b
    else:
        b -= a
else:
    print(a)
