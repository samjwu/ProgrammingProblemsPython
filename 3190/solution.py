from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        min_ops = 0

        for num in nums:
            min_ops += num % 3 != 0

        return min_ops
