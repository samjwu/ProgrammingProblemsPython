class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        nums.sort()
        
        ans = 0
        
        running_freq = 0
        
        for i in range(1, n):
            if nums[i-1] != nums[i]:
                running_freq += 1
                
            ans += running_freq
        
        return ans
