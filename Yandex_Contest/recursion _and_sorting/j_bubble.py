# Яндекс Контест Задача J. "Пузырёк."

n = int(input())
mas = list(map(int, input().split()))

flag = False
flag_2 = False

for j in range(n-1):
    flag = False
    for i in range(n-1-j):
        if mas[i] > mas[i+1]:
            flag = True
            flag_2 = True
            mas[i], mas[i+1] = mas[i+1], mas[i]
    if not flag:
        break
    else:
        print(*mas)

if not flag_2:
    print(*mas)
