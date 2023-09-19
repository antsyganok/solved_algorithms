n, m = map(int, input().split())
lst = []

for _ in range(n):
    lst.append(input())

counter = 0

for i in range(n):
    for j in range(m):
        if lst[i][j] == '*':
            continue
        if lst[i][j - bool(j % m)] == '*':
            continue
        if lst[i][j + bool((j+1) % m)] == '*':
            continue
        if lst[i - bool(i % n)][j] == '*':
            continue
        if lst[i + bool((i+1) % n)][j] == '*':
            continue
        counter += 1

print(counter)
