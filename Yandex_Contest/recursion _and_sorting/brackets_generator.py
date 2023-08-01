# Яндекс Контест Задача A. "Генератор скобок."

def gen_binary(prefix, n, counter=1):

    if n == 0:
        print(prefix)
        return
    if counter < n:
        gen_binary(prefix + '(', n - 1, counter+1)
    if counter > 0:
        gen_binary(prefix + ')', n - 1, counter-1)


def main():
    n = int(input())
    prefix = '('
    bracket_lft = n*2-1
    gen_binary(prefix, bracket_lft)


if __name__ == '__main__':
    main()
