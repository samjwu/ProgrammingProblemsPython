class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        numset = set()
        
        n = len(nums)
        
        for i in range(1, n+1):
            numset.add(i)
            
        duplicate = -1
        missing = -1
            
        for num in nums:
            if num not in numset:
                duplicate = num
            else:
                numset.remove(num)
            
        return [duplicate] + list(numset)
