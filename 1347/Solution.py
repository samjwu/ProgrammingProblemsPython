class Solution:
    def minSteps(self, s: str, t: str) -> int:
        diff = [0 for i in range(26)]
        
        for c in s:
            diff[ord(c) - ord('a')] -= 1
            
        # cancels out diff from s if char is already there
        # increases needed number if char is missing
        for c in t:
            diff[ord(c) - ord('a')] += 1
            
        ans = 0    
        
        for i in range(26):
            ans += max(0, diff[i])
            
        return ans
