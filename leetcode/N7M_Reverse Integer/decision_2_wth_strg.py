""" Runtime:
34 ms
Beats 80.56%

Memory:
17.68 MB
Beats 52.54%
"""


class Solution:
    def reverse(self, x: int) -> int:
        BG = 2147483648

        if x < 0:
            x = int(str(x)[:0:-1]) * -1
            return x if (BG) * -1 <= x else 0
        else:
            x = int(str(x)[::-1])
            return x if (BG) - 1 >= x else 0
