""" Runtime:
31 ms
Beats 91.74%

Memory:
17.99 MB
Beats 10.79%
"""


def reverse(x: int) -> int:
    if x < 0:
        x = int(str(x)[:0:-1]) * -1
        return x if 2147483648 * -1 <= x else 0
    else:
        x = int(str(x)[::-1])
        return x if 2147483648 - 1 >= x else 0
