class Solution:
    def minimumLength(self, s: str) -> int:
        n = len(s)
        
        start = 0
        end = n - 1
        
        while end > start and s[start] == s[end]:
            common = s[start]
            
            while end >= start and s[start] == common:
                start += 1
                
            while end > start and s[end] == common:
                end -= 1
            
        return end - start + 1
