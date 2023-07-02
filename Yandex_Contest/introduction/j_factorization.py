# Яндекс Контест Задача J. "Факторизация."

def simple(number):
    divider = 2
    result = []
    while number % divider == 0:
        result.append(divider)
        number //= divider
    for i in range(3, int(number**0.5)+1, 2):
        while number % i == 0:
            result.append(i)
            number = number // i
    if number > 2:
        result.append(number)

    return print(" ".join(map(str, result)))


simple(int(input()))
