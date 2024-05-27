class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        nums.sort()
        
        for i in range(1, n+1):
            idx = bisect_left(nums, i)
            
            if n-idx == i:
                return i
            
        return -1
