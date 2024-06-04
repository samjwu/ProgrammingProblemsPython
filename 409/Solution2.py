class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        
        for c in s:
            freq[c] = freq.get(c, 0) + 1
            
        ans = 0
        hasOdd = False
        
        for c in freq.keys():
            if freq[c] % 2 == 0:
                ans += freq[c]
            else:
                ans += freq[c]-1
                hasOdd = True
                
        if hasOdd:
            ans += 1
        return ans
