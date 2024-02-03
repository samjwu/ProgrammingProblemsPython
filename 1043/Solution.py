class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.n = len(arr)
        
        self.memo = [-1 for i in range(self.n)]
        
        return self.recurse(arr, k, 0)
    
    def recurse(self, arr: List[int], k: int, idx: int) -> int:
        if idx == self.n:
            return 0
        
        if self.memo[idx] != -1:
            return self.memo[idx]
        
        ans = 0
        subans = 0
        
        for i in range(idx, min(self.n, idx + k)):
            subans = max(subans, arr[i])
            
            ans = max(ans, subans * (i - idx + 1) + self.recurse(arr, k, i + 1))
            
        self.memo[idx] = ans
        return ans
