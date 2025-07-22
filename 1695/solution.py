from collections import defaultdict
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        window = defaultdict(int)
        left = 0
        n = len(nums)
        window_sum = 0
        max_score = 0

        for right in range(n):
            while window[nums[right]] > 0:
                window[nums[left]] -= 1
                window_sum -= nums[left]
                left += 1
            
            window[nums[right]] += 1
            window_sum += nums[right]

            max_score = max(max_score, window_sum)

        return max_score
