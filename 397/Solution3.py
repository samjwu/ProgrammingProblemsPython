class Solution:
    def integerReplacement(self, n: int) -> int:
        memo = {}
        
        def recurse(n: int) -> int:
            if n == 1:
                return 0
            
            if n in memo:
                return memo[n]
            
            if n % 2 == 0:
                memo[n] = 1 + recurse(n/2)
            else:
                memo[n] = 1 + min(recurse(n-1), recurse(n+1))
                
            return memo[n]
            
        return recurse(n)
