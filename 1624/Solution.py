class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        indexDict = {}
        
        n = len(s)
        
        ans = -1
        
        for i in range(n):
            if s[i] in indexDict.keys():
                ans = max(ans, i - indexDict[s[i]] - 1)
            else:
                indexDict[s[i]] = i
            
        return ans
