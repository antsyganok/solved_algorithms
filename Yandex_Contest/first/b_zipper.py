# Яндекс Контест Задача B. "Застёжка-молния."

n = int(input())
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))


def foo(lst_1, lst_2, numb):
    lst_3 = []
    for i in range(0, numb):
        lst_3.append(lst_1[i])
        lst_3.append(lst_2[i])
    return print(*lst_3)


foo(a, b, n)
