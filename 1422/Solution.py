class Solution:
    def maxScore(self, s: str) -> int:
        left = 0
        right = 0
        
        for c in s:
            if c == "1":
                right += 1
           
        ans = 0
        
        n = len(s)
    
        for i in range(n-1):
            c = s[i]
            
            if c == "0":
                left += 1
            else:
                right -= 1
            
            ans = max(ans, left + right)
            
        return ans
