class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map1 = {}
        map2 = {}
        
        n = len(s)
        
        for i in range(n):
            if (s[i] in map1.keys() and map1[s[i]] != t[i]) or (t[i] in map2.keys() and map2[t[i]] != s[i]):
                return False
            
            map1[s[i]] = t[i]
            map2[t[i]] = s[i]
            
        return True
