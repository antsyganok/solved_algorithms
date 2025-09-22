def intToRoman(num: int) -> str:
    values = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    numerals = (
        'M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'
        )

    result = []
    for i in range(len(values)):
        count = num // values[i]
        if count > 0:
            result.append(numerals[i] * count)
            num %= values[i]
            if num == 0:
                break

    return ''.join(result)
