class Solution:
    def numSquares(self, n: int) -> int:
        self.memo = [-1 for i in range(n+1)]
        return self.recurse(n)

    def recurse(self, n: int) -> int:
        if n < 4:
            return n
        
        if self.memo[n] != -1:
            return self.memo[n]
        
        ans = n
        i = 1
        while i*i <= n:
            ans = min(ans, 1 + self.recurse(n - i*i))
            i += 1
            
        self.memo[n] = ans
        return ans
