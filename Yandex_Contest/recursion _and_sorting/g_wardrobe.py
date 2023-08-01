# Яндекс Контест Задача G. "Гардероб."

def main(array, k):
    result = ['1']*k
    pointer_zero = 0
    pointer_two = k-1
    for i in range(0, len(array), 2):
        if array[i] == '0':
            result[pointer_zero] = '0'
            pointer_zero += 1
        elif array[i] == '2':
            result[pointer_two] = '2'
            pointer_two -= 1
    return result


if __name__ == '__main__':

    k = int(input())
    array = input()
    print(*main(array, k))
