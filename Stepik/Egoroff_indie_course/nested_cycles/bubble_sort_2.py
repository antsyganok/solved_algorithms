n = int(input())
lst = list(map(int, input().split()))

counter = 0

while True:
    flag = 0
    for i in range(n-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
            counter += 1
            flag += 1
    if flag < 1:
        break

print(*lst, f'\n{counter}')
