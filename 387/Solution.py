class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = set()
        repeat = set()
        
        for c in s:
            if c in seen:
                repeat.add(c)
            seen.add(c)
        
        n = len(s)
        
        for i in range(n):
            if s[i] not in repeat:
                return i
            
        return -1
