# Яндекс Контест Задача I. "Степень четырёх." (альтернативное решение)

from math import log


def is_power_of_four(number: int) -> bool:
    return (log(number, 4)).is_integer()  # arg, base


print(is_power_of_four(int(input())))
