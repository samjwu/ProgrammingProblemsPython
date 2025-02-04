class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        cur = nums[0]
        n = len(nums)

        for i in range(1, n):
            if nums[i-1] >= nums[i]:
                ans = max(ans, cur)
                cur = 0
            cur += nums[i]

        return max(ans, cur)
