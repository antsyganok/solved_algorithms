# Яндекс Контест Задача С. "Скользящее среднее."

n = int(input())
arr = list(map(int, input().strip().split()))
k = int(input())


def foo(n, arr, K):
    result = []
    current_sum = sum(arr[0:K])
    result.append(current_sum / K)

    for i in range(0, n-K):
        current_sum -= arr[i]
        current_sum += arr[i+K]

        current_avg = current_sum / K
        result.append(current_avg)
    return print(*result)


foo(n, arr, k)
