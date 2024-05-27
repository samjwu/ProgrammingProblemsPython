class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        nums.sort()
        
        def bisectLeft(val: int) -> int:
            l = 0
            r = n-1
            
            while l <= r:
                m = l + (r - l) // 2
                
                if nums[m] >= val:
                    r = m-1
                else:
                    l = m+1
                    
            return l
        
        for i in range(1, n+1):
            idx = bisectLeft(i)
            
            if n-idx == i:
                return i
            
        return -1
