# Яндекс Контест Задача K. "Рекурсивные числа Фибоначчи."

def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1)+fib(n-2)


n = int(input()) + 1
print(fib(n))
