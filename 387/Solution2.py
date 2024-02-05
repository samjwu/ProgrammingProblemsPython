class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = defaultdict(int)
        
        for c in s:
            freq[c] += 1
        
        n = len(s)
        
        for i in range(n):
            if freq[s[i]] == 1:
                return i
            
        return -1
