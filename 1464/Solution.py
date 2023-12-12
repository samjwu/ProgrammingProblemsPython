class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        hi = -1
        hi2 = -1
        
        for num in nums:
            if num >= hi:
                hi2 = hi
                hi = num
            else:
                hi2 = max(hi2, num)
        
        return (hi - 1) * (hi2 - 1)
