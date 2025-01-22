""" Runtime:
41 ms
Beats 37.05%

Memory:
17.88 MB
Beats 23.45%
 """


class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            x = int(str(x)[:0:-1]) * -1
        else:
            x = int(str(x)[::-1])

        return x if x.bit_length() < 32 else 0
