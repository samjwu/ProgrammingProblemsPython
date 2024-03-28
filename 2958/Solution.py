class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        
        n = len(nums)
        
        freq = Counter()
        
        left = -1
        
        for right in range(n):
            freq[nums[right]] += 1
            
            while freq[nums[right]] > k:
                left += 1
                freq[nums[left]] -= 1
                
            ans = max(ans, right - left)
            
        return ans
