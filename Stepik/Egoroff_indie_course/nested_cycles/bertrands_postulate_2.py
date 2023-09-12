n = int(input())
rez = 0

for i in range(n+1, n*2):
    j = 1
    counter = 0
    while j*j <= i:
        if i % j == 0:
            counter += 1
            if j != i//j:
                counter += 1
        j += 1
    if counter == 2:
        rez += 1

print(rez)
