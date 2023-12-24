class Solution:
    def minOperations(self, s: str) -> int:
        start1 = 0
        
        n = len(s)
        
        for i in range(n):
            if i % 2 == 0:
                if s[i] == "0":
                    start1 += 1
            else:
                if s[i] == "1":
                    start1 += 1
                
        return min(n - start1, start1)
