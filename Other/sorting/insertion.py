

def InsertionSort(data: list[int | float]) -> list[int | float]:
    """
    сортировка вставками
    """
    numbers = data.copy()

    for i in range(1, len(numbers)):
        elem = numbers[i]
        j = i-1

        while j >= 0 and numbers[j] > elem:
            numbers[j+1] = numbers[j]
            j -= 1

        numbers[j + 1] = elem
    return numbers

if __name__ == "__main__":
    arr_numbers = [42, 17, 3, 88, -2, 1002, 0, 5, 72, 10, 1.5, 3, 56, 29]
    print(InsertionSort(arr_numbers))
