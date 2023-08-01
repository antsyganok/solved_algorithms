# Яндекс Контест Задача K. "Клумбы."

gardener = int(input())
seq = [list(map(int, input().split())) for _ in range(gardener)]
seq.sort()
new_seq = []
head = seq[0][0]
tail = seq[0][1]

for s in seq:
    if s[0] > tail:
        new_seq.append([head, tail])
        head, tail = s[0], s[1]
    else:
        if s[1] > tail:
            tail = s[1]
new_seq.append([head, tail])
for new in new_seq:
    print(*new)
