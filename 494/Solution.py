class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        memo = {}
        
        def recurse(idx, nums, target, val):
            if (idx, val) in memo:
                return memo[(idx, val)]
            
            if idx == n:
                if val == target:
                    return 1
                return 0
            
            plus = recurse(idx+1, nums, target, val + nums[idx])
            minus = recurse(idx+1, nums, target, val - nums[idx])
            
            memo[(idx,val)] = plus + minus
            return memo[(idx,val)]
                    
        return recurse(0, nums, target, 0)
