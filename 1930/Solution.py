class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        ans = 0
        
        unique_letters = set()  
        for c in s:
            unique_letters.add(c)
        
        for letter in unique_letters:
            left = -1
            right = 0
            
            for i in range(n):
                if s[i] == letter:
                    if left == -1:
                        left = i
                    right = i
            
            between = set()
            for j in range(left+1, right):
                between.add(s[j])
                
            ans += len(between)
        
        return ans
