class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        target = total // 2
        
        # memo[x] = true if can form subset with sum x
        memo = [False] * (target+1)
        memo[0] = True
        
        for num in nums:
            for j in range(target, num-1, -1):
                memo[j] = memo[j] or memo[j-num]
        
        return memo[target]
