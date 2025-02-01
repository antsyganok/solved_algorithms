""" Runtime:
29 ms
Beats 94.74%

Memory:
17.75 MB
Beats 36.43%
 """


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = int(str(x)[:0:-1]) * -1
            return x if (2 ** 31) * -1 <= x else 0
        else:
            x = int(str(x)[::-1])
            return x if (2 ** 31) - 1 >= x else 0
