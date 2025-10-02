"""
Runtime:
8 ms
Beats 48.89%

Memory:
22.17 MB
Beats 5.28%
"""
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    intervals = [[min(i[0], i[1]), max(i[0], i[1])] for i in intervals]
    intervals.sort(key=lambda x: x[0])
    res = [intervals[0]]

    for ind in range(1, len(intervals)):
        curr = intervals[ind]
        last_res = res[-1]

        if curr[0] <= last_res[1]:
            last_res[1] = max(last_res[1], curr[1])
        else:
            res.append(curr)

    return res
