from typing import List


class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        min_avg = float("inf")
        n = len(nums)

        nums.sort()

        for i in range(n // 2):
            avg = (nums[i] + nums[n-1-i]) / 2
            min_avg = min(min_avg, avg)

        return min_avg
