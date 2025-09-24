"""
26 ms
Beats 81.91%

Memory:
29.43 MB
Beats 30.4%
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) == 0 or nums[0] > 1:
            return 1

        val = 1
        for i in nums:
            if i == val:
                val += 1

        return val
