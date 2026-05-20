
def bubble_sort(data: list[int]) -> list[int]:
    """
    Сортирует массив чисел методом пузырька (Bubble Sort) in-place.

    Алгоритм последовательно сравнивает соседние элементы и меняет их местами,
    если предыдущий элемент больше последующего. В результате больших проходов
    максимальные элементы "всплывают" в конец массива.
    """

    numbers = data.copy()

    for _ in range(len(numbers) - 1):
        for i in range(1, len(numbers)):
            if numbers[i-1] > numbers[i]:
                numbers[i-1], numbers[i] = numbers[i], numbers[i-1]

    return numbers


if __name__ == "__main__":
    arr_numbers = [42, 17, 3, 88, -2, 1000, 0, 5, 72, 10, 1.5, 3, 56, 29]
    print(bubble_sort(arr_numbers))
