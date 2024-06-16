class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0
        
        miss = 1
        
        idx = 0
        
        while miss <= n:
            # nums up to idx sum up to miss
            # so add current num to open range
            if idx < len(nums) and nums[idx] <= miss:
                miss += nums[idx]
                idx += 1
                
            # nums up to idx do not sum up to miss
            # so add missing num to nums
            # which doubles the open range
            else:
                miss += miss
                ans += 1
                
        return ans
