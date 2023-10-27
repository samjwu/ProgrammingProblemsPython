class Solution:
    def longestPalindrome(self, s: str) -> str:
        endpoints = [0, 0]

        for i in range(len(s)):
            odd_len = self.longest_at(s, i, i)
            if odd_len > endpoints[1] - endpoints[0] + 1:
                half_len = odd_len // 2
                endpoints = [i - half_len, i + half_len]

            even_len = self.longest_at(s, i, i+1)
            if even_len > endpoints[1] - endpoints[0] + 1:
                half_len = (even_len // 2) - 1
                endpoints = [i - half_len, i+1 + half_len]
        
        return s[endpoints[0]:endpoints[1]+1]
    
    # starting from i, j as center point
    # return length-2 of longest palindrome
    def longest_at(self, s: str, left: int, right: int) -> int:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1
