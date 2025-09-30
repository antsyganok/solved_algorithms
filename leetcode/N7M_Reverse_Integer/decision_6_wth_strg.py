""" Runtime:
31 ms
Beats 91.74%

Memory:
17.76 MB
Beats 36.43%
"""


def reverse(x: int) -> int:
    if x < 0:
        x = int(str(x)[:0:-1]) * -1
    else:
        x = int(str(x)[::-1])

    return x if x.bit_length() < 32 else 0
