class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        n = len(words)
        
        freq = [[0 for j in range(26)] for i in range(n)]
        
        for i in range(n):
            for c in words[i]:
                idx = ord(c) - ord("a")
                freq[i][idx] += 1
                
        ans = []
        
        for j in range(26):
            allCount = float("inf")
            
            for i in range(n):
                allCount = min(allCount, freq[i][j])
                
            for k in range(allCount):
                ans.append(chr(ord("a") + j))
                
        return ans
