class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        
        if n == 2:
            return 1
        
        t0 = 0
        t1 = 1
        t2 = 1
        t3 = 0
        
        for i in range(2, n):
            t3 = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = t3
            
        return t3
