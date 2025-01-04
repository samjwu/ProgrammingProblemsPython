class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)

        first = [-1] * 26
        last = [-1] * 26
        
        for i in range(len(s)):
            letter = ord(s[i]) - ord("a")

            if first[letter] == -1:
                first[letter] = i
            
            last[letter] = i
        
        ans = 0

        for i in range(26):
            if first[i] == -1:
                continue
                
            middle = set()

            for j in range(first[i] + 1, last[i]):
                middle.add(s[j])
            
            ans += len(middle)

        return ans
