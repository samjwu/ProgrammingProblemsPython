class Solution:
    def integerReplacement(self, n: int) -> int:
        return self.recurse(n, 0)
    
    def recurse(self, n: int, ops: int) -> int:
        if n == 1:
            return ops
        
        if n % 2 == 0:
            return self.recurse(n/2, ops+1)
        
        op1 = self.recurse(n-1, ops+1)
        op2 = self.recurse(n+1, ops+1)
        
        return min(op1, op2)
