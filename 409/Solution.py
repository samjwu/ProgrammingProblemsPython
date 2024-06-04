class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = defaultdict(int)
        chars = set()
        
        for c in s:
            freq[c] += 1
            chars.add(c)
            
        ans = 0
        hasOdd = False
        
        for c in chars:
            if freq[c] % 2 == 0:
                ans += freq[c]
            else:
                ans += freq[c]-1
                hasOdd = True
                
        if hasOdd:
            ans += 1
        return ans
