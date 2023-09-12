lenth = int(input())
lst = list(map(int, input().split()))
res = [0]*201
res_2 = ''

for i in lst:
    res[i+100] += 1

for j in range(len(res)):
    if res[j] > 0:
        res_2 += (str(j-100) + ' ') * res[j]

print(res_2)
