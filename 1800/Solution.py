class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ans = 0
        idx = 0
        n = len(nums)
        cur = 0

        while idx < n:
            cur = nums[idx]
            while idx < n-1 and nums[idx] < nums[idx+1]:
                cur += nums[idx+1]
                idx += 1
            ans = max(ans, cur)
            idx += 1

        return ans
