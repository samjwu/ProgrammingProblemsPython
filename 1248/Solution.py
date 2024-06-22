class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        l = 0
        
        ans = 0
        subans = 0
        odd = 0
        
        for r in range(n):
            if nums[r] % 2 == 1:
                odd += 1
                subans = 0
            
            while odd == k:
                subans += 1
                
                if nums[l] % 2 == 1:
                    odd -= 1
                
                l += 1
                
            ans += subans
            
        return ans
