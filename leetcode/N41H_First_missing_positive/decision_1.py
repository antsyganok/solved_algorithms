"""
23 ms
Beats 87.61%

Memory:
34.74 MB
Beats 11.69%
"""
from typing import List


def firstMissingPositive(nums: List[int]) -> int:
    nums = set(nums)
    mx = min(max(nums, default=0), int(3e9))

    for i in range(1, mx):
        if i not in nums:
            return i
    return 1 if mx < 0 else mx + 1
