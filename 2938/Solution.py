class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        
        idx = 0
        
        ans = 0
        
        for i in range(n):
            if s[i] == '0':
                ans += i - idx
                
                idx += 1
                
        return ans
