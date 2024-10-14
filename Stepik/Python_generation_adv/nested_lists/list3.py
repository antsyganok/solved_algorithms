"""
Дополните приведенный код,
используя цикл for и встроенную функцию max(),
чтобы он выводил максимальный элемент среди всех
элементов вложенных списков списка list1.

вар 2:

list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = [max(nums) for nums in list1]

print(max(maximum))
"""

list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = 0

for nums in list1:
    temp = max(nums)
    if maximum < temp:
        maximum = temp

print(maximum)
