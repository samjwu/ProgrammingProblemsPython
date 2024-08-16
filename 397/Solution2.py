class Solution:
    def integerReplacement(self, n: int) -> int:
        self.memo = {}
        return self.recurse(n)
    
    def recurse(self, n: int) -> int:
        if n == 1:
            return 0
        
        if n in self.memo:
            return self.memo[n]
        
        if n % 2 == 0:
            self.memo[n] = 1 + self.recurse(n/2)
        else:
            self.memo[n] = 1 + min(self.recurse(n-1), self.recurse(n+1))
        
        return self.memo[n]
