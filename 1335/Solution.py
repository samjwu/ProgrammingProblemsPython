class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        self.n = len(jobDifficulty)
    
        if self.n < d:
            return -1
        
        self.memo = [[-1 for j in range(d+1)] for i in range(self.n)]
        
        return self.dfs(d, 0, jobDifficulty)
    
    def dfs(self, days: int, idx: int, jobDifficulty: List[int]) -> int:
        if days == 0 and idx == self.n:
            return 0
        
        if days == 0 or idx == self.n:
            return inf
        
        if self.memo[idx][days] != -1:
            return self.memo[idx][days]
        
        currMax = jobDifficulty[idx]
        subAns = inf
        
        for i in range(idx, self.n):
            currMax = max(currMax, jobDifficulty[i])
            
            tmp = self.dfs(days-1, i+1, jobDifficulty)
            if tmp != inf:
                subAns = min(subAns, tmp + currMax)
        
        self.memo[idx][days] = subAns
        return subAns
