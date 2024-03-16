class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        
        ans = 0
        
        balance = {}
        
        balance[0] = -1
        
        count = 0
        
        for i in range(n):
            if nums[i] == 1:
                count += 1
            else:
                count -= 1
                
            if count in balance:
                ans = max(ans, i - balance[count])
            else:
                balance[count] = i
                
        return ans
