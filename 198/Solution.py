class Solution:
    def rob(self, nums: List[int]) -> int:
        self.n = len(nums)
        
        self.memo = [-1 for i in range(self.n)]
        
        return self.dfs(nums, 0)
        
    def dfs(self, nums: List[int], idx: int) -> int:
        if idx >= self.n:
            return 0
        
        if self.memo[idx] != -1:
            return self.memo[idx]
        
        take = self.dfs(nums, idx+2) + nums[idx]
        skip = self.dfs(nums, idx+1)
        
        self.memo[idx] = max(take, skip)
        return self.memo[idx]
        