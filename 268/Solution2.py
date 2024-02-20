class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        
        n = len(nums)
        
        for i in range(n+1):
            total += i
            
        for num in nums:
            total -= num
            
        return total
