# Яндекс Контест Задача G. "Работа из дома."

number = (int(input()))
result = ''
if number == 0:
    print(number)
while number > 0:
    result += str(number % 2)
    number //= 2
print(result[::-1])
