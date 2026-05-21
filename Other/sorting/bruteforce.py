

def selectionSort(data: list[int]) -> list[int]:
    """
    Сортирует массив целых чисел методом перебора (выбора).

    Алгоритм находит минимальные элементы, извлекает их из копии
    исходного списка и формирует новый, упорядоченный массив.
    Оригинальный список при этом не изменяется.
    """
    numbers = data.copy()
    new_numbers = []

    while len(numbers) > 0:
        minval = 0
        for i in range(1, len(numbers)):
            if numbers[i] < numbers[minval]:
                minval = i

        minnum = numbers.pop(minval)
        new_numbers.append(minnum)

    return new_numbers

if __name__ == "__main__":
    arr_numbers = [42, 17, 3, 88, 5, 72, 10, 3, 56, 29]
    print(selectionSort(arr_numbers))
