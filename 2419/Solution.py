class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        hi = 0
        curr = 0
        ans = 0
        
        for num in nums:
            if hi < num:
                hi = num
                curr = 0
                ans = 0
                
            if hi == num:
                curr += 1
            else:
                curr = 0
                
            ans = max(ans, curr)
            
        return ans
