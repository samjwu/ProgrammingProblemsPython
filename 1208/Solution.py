class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        n = len(s)
        
        ans = 0
        
        currCost = 0
        
        # sliding window
        left = 0
        for right in range(n):
            currCost += abs(ord(s[right]) - ord(t[right]))
            
            while currCost > maxCost:
                currCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            
            ans = max(ans, right - left + 1)
        
        return ans
