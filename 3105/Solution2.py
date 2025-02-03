class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1

        incr = 1
        decr = 1

        for i in range(n-1):
            incr = incr + 1 if nums[i] < nums[i+1] else 1
            decr = decr + 1 if nums[i] > nums[i+1] else 1
            ans = max(ans, incr, decr)

        return ans
