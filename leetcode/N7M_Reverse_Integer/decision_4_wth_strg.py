""" Runtime:
41 ms
Beats 37.05%

Memory:
17.86 MB
Beats 23.45%
"""


def reverse(x: int) -> int:

    if x < 0:
        x = int(str(x)[:0:-1]) * -1
        return x if -2147483648 <= x else 0
    else:
        x = int(str(x)[::-1])
        return x if 2147483647 >= x else 0
