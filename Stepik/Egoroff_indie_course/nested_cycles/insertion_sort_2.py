size = int(input())
lst = list(map(int, input().split()))

for i in range(1, size):
    for j in range(i):
        temp = lst[j]
        if lst[i] < lst[j]:
            lst[j] = lst[i]
            lst[i] = temp

print(*lst)
