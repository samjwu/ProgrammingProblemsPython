class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)

        if n <= 4:
            return 0

        nums.sort()

        ans = float("inf")

        for l in range(4):
            r = n-1 - 3 + l
            ans = min(ans, nums[r] - nums[l])

        return ans
