# функция merge_two_list должна объединить два списка
def merge_two_list(a: list, b: list) -> list:
    """слияние двух отсортированных по неубыванию списков"""
    res = []

    while a and b:
        if a[0] >= b[0]:
            res.append(b.pop(0))
        else:
            res.append(a.pop(0))
    res += a + b

    return res


# функция merge_sort должна выполнить сортировку
def merge_sort(s: list) -> list:
    """сортировка слиянием"""
    if len(s) <= 1:
        return s

    mid = len(s) // 2

    l_arr = merge_sort(s[:mid])
    r_arr = merge_sort(s[mid:])

    return merge_two_list(l_arr, r_arr)
