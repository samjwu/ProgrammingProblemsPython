class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        hi = 0
        hi2 = 0
        lo = inf
        lo2 = inf
        
        for num in nums:
            if num > hi:
                hi2 = hi
                hi = num
            else:
                hi2 = max(hi2, num)
                
            if num < lo:
                lo2 = lo
                lo = num
            else:
                lo2 = min(lo2, num)
        
        return hi*hi2 - lo*lo2
