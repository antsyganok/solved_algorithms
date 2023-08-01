# Яндекс Контест Задача K. "Сортировка слиянием."

def merge(arr, lf, mid, rg):
    res = [None] * (rg - lf)
    i = 0
    static_mid = mid

    while mid < rg and lf < static_mid:
        if arr[mid] <= arr[lf]:
            res[i] = arr[mid]
            mid += 1
        else:
            res[i] = arr[lf]
            lf += 1
        i += 1
    while mid < rg:
        res[i] = arr[mid]
        mid += 1
        i += 1
    while lf < static_mid:
        res[i] = arr[lf]
        lf += 1
        i += 1

    return res


def merge_sort(arr, lf, rg):
    mid = (rg + lf) // 2
    if rg - lf == 1:
        return
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)

    res = merge(arr, lf, mid, rg)

    for i in res:
        arr[lf] = i
        lf += 1


def test():
    a = [1, 4, 9, 2, 10, 11]
    b = merge(a, 0, 3, 6)
    expected = [1, 2, 4, 9, 10, 11]
    assert b == expected

    c = [1, 4, 2, 10, 1, 2]
    merge_sort(c, 0, 6)
    expected = [1, 1, 2, 2, 4, 10]
    assert c == expected


if __name__ == '__main__':
    test()
