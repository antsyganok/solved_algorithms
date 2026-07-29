

def insertion_sort(data: list[int | float]) -> list[int | float]:
    """
    Сортирует список чисел методом вставок, возвращая новый массив.

    Разделяет массив на отсортированную и неотсортированную части.
    На каждом шаге берет элемент из конца и вставляет его на
    нужное место в отсортированную часть, сдвигая большие элементы вправо.

    Эффективен для малых (до десятков элементов) или частично
    отсортированных данных. Устойчив, работает без затрат доп. памяти.
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
    print(insertion_sort(arr_numbers))
