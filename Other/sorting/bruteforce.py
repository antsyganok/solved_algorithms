"""

"""


def bruteforce(data):

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


arr_numbers = [42, 17, 3, 88, 5, 72, 10, 3, 56, 29]

print(bruteforce(arr_numbers))
