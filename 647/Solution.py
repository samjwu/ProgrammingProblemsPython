class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        
        # if substr from start to end inclusive is palindrome,
        # memo[start][end] = True 
        memo = [defaultdict(bool) for i in range(n+1)]
        
        ans = 0
        
        # single chars are always palindromes
        for i in range(n):
            memo[i][i] = True
            ans += 1
            
        # check 2 char palindromes
        for i in range(n-1):
            if s[i] == s[i+1]:
                memo[i][i+1] = True
                ans += 1
                
        # check 3+ char palindromes
        for length in range(3, n+1):
            start = 0
            end = start + length-1
            
            while end < n:
                if s[start] == s[end] and memo[start+1][end-1] == True:
                    memo[start][end] = True
                    ans += 1
                    
                start += 1
                end += 1
                
        return ans
