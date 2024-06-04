class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        
        unpairedChars = 0
        
        for c in s:
            freq[c] = freq.get(c, 0) + 1
            
            if freq[c] % 2 == 1:
                unpairedChars += 1
            else:
                unpairedChars -= 1
            
        n = len(s)
        
        if unpairedChars > 0:
            return n - unpairedChars + 1
        else:
            return n
