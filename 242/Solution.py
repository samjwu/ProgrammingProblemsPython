class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chars_s = defaultdict(int)
        chars_t = defaultdict(int)
        
        for c in s:
            chars_s[c] += 1
            
        for c in t:
            chars_t[c] += 1
            
        for i in range(26):
            c = chr(ord('a') + i)
            if chars_s[c] != chars_t[c]:
                return False
            
        return True
