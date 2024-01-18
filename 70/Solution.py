class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        memo = [0 for i in range(n+1)]
        
        memo[1] = 1
        memo[2] = 2
        
        for i in range(3, n+1):
            memo[i] = memo[i-2] + memo[i-1]
            
        return memo[n]
