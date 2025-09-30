"""
Runtime:
41 ms
Beats 37.05%

Memory:
17.88 MB
Beats 23.45%
"""


def reverse(x: int) -> int:
    num = 2147483648
    flg = False

    if x < 0:
        x = -x
        flg = True
    x = int(str(x)[::-1])
    if flg:
        x = -x

    return x if -num <= x <= num-1 else 0
