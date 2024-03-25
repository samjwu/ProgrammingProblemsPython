class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        ans = []
        
        for i in range(n):
            idx = abs(nums[i]) - 1
            
            if nums[idx] < 0:
                ans.append(idx + 1)
            else:
                nums[idx] *= -1
        
        return ans
