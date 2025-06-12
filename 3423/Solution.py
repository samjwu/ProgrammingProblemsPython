class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = len(nums)
        max_diff = 0

        for i in range(n):
            max_diff = max(max_diff, abs(nums[i-1] - nums[i]))

        return max_diff
