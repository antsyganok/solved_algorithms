""" Runtime:
31 ms
Beats 91.74%

Memory:
17.90 MB
Beats 23.45%
"""


class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            x = int(str(x)[:0:-1]) * -1
            return x if -2**31 <= x else 0
        else:
            x = int(str(x)[::-1])
            return x if (2**31) - 1 >= x else 0
