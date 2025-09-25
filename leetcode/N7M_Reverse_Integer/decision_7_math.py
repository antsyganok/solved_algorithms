"""
Runtime:
23 ms
Beats 99.08%

Memory:
17.84 MB
Beats 36.92%
"""


def reverse(x: int) -> int:
    reslt = 0
    sign = -1 if x < 0 else 1
    x = abs(x)

    while x > 0:
        reslt = reslt * 10 + x % 10
        x //= 10

    reslt *= sign
    return reslt if -2**31 <= reslt <= 2**31 - 1 else 0
