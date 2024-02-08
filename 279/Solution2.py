class Solution:
    def numSquares(self, n: int) -> int:
        memo = [float('inf') for i in range(n+1)]
        
        memo[0] = 0
        
        for i in range(n+1):
            j = 1
            
            while j*j <= i:
                memo[i] = min(memo[i], memo[i - j*j] + 1)
                j += 1
            
        return memo[n]
