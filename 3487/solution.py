from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        high = max(nums)

        if high <= 0:
            return high

        max_sum = 0
        seen = set()

        for num in nums:
            if num > 0 and num not in seen:
                max_sum += num
                seen.add(num)

        return max_sum
