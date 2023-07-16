# Яндекс Контест Задача A. "Мониторинг."

n = int(input())
m = int(input())
# numbers = []  # Получил TL, переделал
# for i in range(n):
#     numbers.append(list(map(int, input().strip().split())))
numbers = ''
numbers = [input().split(' ') for j in range(n)]

for i in range(m):
    for j in range(n):
        print(numbers[j][i], end=' ')
    print()
