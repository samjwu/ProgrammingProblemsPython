from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = -1
        min_so_far = nums[0]

        for i in range(1, n):
            if nums[i] > min_so_far:
                max_diff = max(max_diff, nums[i] - min_so_far)
            else:
                min_so_far = nums[i]

        return max_diff
