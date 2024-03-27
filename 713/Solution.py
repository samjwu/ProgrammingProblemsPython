class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        
        n = len(nums)
        
        ans = 0
        
        prod = 1
        
        left = 0
        
        for right in range(n):
            prod *= nums[right]
            
            while prod >= k:
                prod //= nums[left]
                left += 1
                
            # add number of subarrays starting at left
            ans += right - left + 1
            
        return ans
