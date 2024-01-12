class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aeiouAEIOU"
        
        n = len(s)
        
        l = 0
        r = 0
        
        for i in range(n // 2):
            if s[i] in vowels:
                l += 1
                
            if s[n - 1 - i] in vowels:
                r += 1
        
        return l == r
