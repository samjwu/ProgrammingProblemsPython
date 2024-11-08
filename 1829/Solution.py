class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        ans = []
        
        xor = 0
        for num in nums:
            xor = xor ^ num
            
        k = 2**maximumBit - 1
        n = len(nums)
        for i in range(n-1, -1, -1):
            ans.append(k ^ xor)
            xor = xor ^ nums[i]
        
        return ans
