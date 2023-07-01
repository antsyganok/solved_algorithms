# Яндекс Контест Задача Е. "Две фишки - 2."

n = int(input())
lst = list(map(int, input().strip().split()))
target_sum = int(input())


def two_sum_sort(lst, target_sum):
    lst.sort()

    left = 0
    right = n-1

    while left < right:
        current_sum = lst[left] + lst[right]
        if current_sum == target_sum:
            return print(lst[left], lst[right])
        if current_sum < target_sum:
            left += 1
        else:
            right -= 1
    return print(None)


two_sum_sort(lst, target_sum)
