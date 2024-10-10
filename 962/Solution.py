class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        
        indices = [i for i in range(n)]

        indices.sort(key=lambda i: (nums[i], i))

        lo = n
        
        ans = 0

        for i in indices:
            ans = max(ans, i - lo)
            lo = min(lo, i)

        return ans
