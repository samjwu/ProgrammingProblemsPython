class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        n = len(s)
        
        unique_letters = set()
        left = {}
        right = {}
        
        for i in range(n):
            unique_letters.add(s[i])
            
            if s[i] not in left.keys():
                left[s[i]] = i
                
            right[s[i]] = i
        
        for letter in unique_letters:
            left_idx = left[letter]
            right_idx = right[letter]
            between = set()
            
            for i in range(left_idx+1, right_idx):
                between.add(s[i])
                
            ans += len(between)
        
        return ans
