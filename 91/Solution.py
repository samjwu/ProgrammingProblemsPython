class Solution:
    def numDecodings(self, s: str) -> int:
        self.n = len(s)
        
        self.memo = [-1 for i in range(self.n + 1)]
        
        self.memo[self.n] = 1
        
        return self.numDecodingsAt(s, 0)
        
    def numDecodingsAt(self, s: str, i: int) -> int:
        if self.memo[i] != -1:
            return self.memo[i]
        
        if s[i] == "0":
            return 0
        
        ans = self.numDecodingsAt(s, i+1)
        
        if i < self.n - 1 and (s[i] == "1" or (s[i] == "2" and s[i+1] <= "6")):
            ans += self.numDecodingsAt(s, i+2)
            
        self.memo[i] = ans
        return ans
