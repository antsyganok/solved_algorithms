

def selectionSort(data: list[int]) -> list[int]:
    """
    Сортирует массив целых чисел методом перебора (выбора).

    Алгоритм находит минимальные элементы, извлекает их из копии
    исходного списка и формирует новый, упорядоченный массив.
    Оригинальный список при этом не изменяется.
    """
    numbers = data.copy()
    n = len(numbers)

    for i in range(n):
        minval = i
        for j in range(i+1, n):
            if numbers[j] < numbers[minval]:
                minval = j

        numbers[i], numbers[minval] = numbers[minval], numbers[i]

    return numbers

if __name__ == "__main__":
    arr_numbers = [42, 17, 3, 88, -2, 1002, 0, 5, 72, 10, 1.5, 3, 56, 29]
    print(selectionSort(arr_numbers))
