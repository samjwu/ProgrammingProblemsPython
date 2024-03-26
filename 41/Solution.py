class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        present = [False for i in range(n+1)]
        
        for num in nums:
            if num > 0 and num <= n:
                present[num] = True
                
        for i in range(1, n+1):
            if not present[i]:
                return i
            
        return n+1
