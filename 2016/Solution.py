from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = -1

        for i in range(n):
            for j in range(i+1, n):
                diff = nums[j] - nums[i]
                if diff > max_diff and diff > 0:
                    max_diff = diff

        return max_diff
