class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        
        # specialFreq[i][j] = count of special substring
        # where i is index of char (a-z)
        # and j is length of special substring (0 to n)
        specialFreq = [[0 for j in range(n+1)] for i in range(26)]
        
        ans = -1
        
        i = 0
        
        while i < n:
            currSpecialLen = 1
            
            while i < n-1 and s[i] == s[i+1]:
                currSpecialLen += 1
                i += 1
            
            specialFreq[ord(s[i]) - ord('a')][currSpecialLen] += 1
            if specialFreq[ord(s[i]) - ord('a')][currSpecialLen] >= 3:
                ans = max(ans, currSpecialLen)
            
            if currSpecialLen > 1:
                specialFreq[ord(s[i]) - ord('a')][currSpecialLen-1] += 2
                if specialFreq[ord(s[i]) - ord('a')][currSpecialLen-1] >= 3:
                    ans = max(ans, currSpecialLen-1)
                    
            if currSpecialLen > 2:
                specialFreq[ord(s[i]) - ord('a')][currSpecialLen-2] += 3
                if specialFreq[ord(s[i]) - ord('a')][currSpecialLen-2] >= 3:
                    ans = max(ans, currSpecialLen-2)
            
            i += 1
        
        return ans
