"""
Runtime:
2 ms
Beats 94.58%

Memory:
20.92 MB
Beats 64.83%
"""
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    intervals.sort()
    res = [intervals[0]]

    for ind in range(1, len(intervals)):
        last_res = res[-1]

        if intervals[ind][0] <= last_res[1]:
            last_res[1] = max(last_res[1], intervals[ind][1])
        else:
            res.append(intervals[ind])

    return res
