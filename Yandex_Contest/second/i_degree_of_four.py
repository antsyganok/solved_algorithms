# Яндекс Контест Задача I. "Степень четырёх."

def is_power_of_four(number: int) -> bool:
    compare = 1
    while compare < number:
        compare *= 4
    return compare == number


print(is_power_of_four(int(input())))
