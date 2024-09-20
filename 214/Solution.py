class Solution:
    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        
        rev = s[::-1]
        
        for i in range(n):
            # find longest matching prefix of s and suffix of reversed
            # prepending remaining prefix of reversed to s
            # yields shortest palindrome
            if s[0:n-i] == rev[i:n]:
                return rev[0:i] + s
            
        return ""
