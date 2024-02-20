class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numset = set()
        
        n = len(nums)
        
        for i in range(n+1):
            numset.add(i)
            
        for num in nums:
            numset.remove(num)
            
        return numset.pop()
