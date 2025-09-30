"""
Runtime:
31 ms
Beats 93.66%

Memory:
17.49 MB
Beats 99.79%
"""


def reverse(x: int) -> int:
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31

    reslt = 0
    sign = -1 if x < 0 else 1
    x = abs(x)

    while x > 0:
        reslt = reslt * 10 + x % 10
        x //= 10

    reslt *= sign

    return reslt if INT_MIN <= reslt <= INT_MAX else 0
