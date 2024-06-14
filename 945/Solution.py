class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        
        n = len(nums)
        
        ans = 0
        
        for i in range(n-1):
            if nums[i] >= nums[i+1]:
                add = nums[i] + 1 - nums[i+1]
                nums[i+1] = nums[i] + 1
                ans += add
                
        return ans
