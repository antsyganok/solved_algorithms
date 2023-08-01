# Яндекс Контест Задача H. "Большое число."

num = int(input())
inp = input().split()


def comparatior(obj_1, obj_2):
    x = obj_1 + obj_2
    y = obj_2 + obj_1
    return x < y


def big_number(num, inp):
    for j in range(num-1):
        for i in range(num-1-j):
            if comparatior(inp[i], inp[i+1]):
                inp[i], inp[i+1] = inp[i+1], inp[i]
    return ''.join(map(str, inp))


print(big_number(num, inp))
