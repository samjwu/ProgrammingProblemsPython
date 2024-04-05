class Solution:
    def makeGood(self, s: str) -> str:
        ans = ""
        
        for c in s:
            if ans and self.isBad(ans[-1], c):
                ans = ans[:-1]
            else:
                ans += c
                
        return ans
    
    def isBad(self, a: str, b: str) -> bool:
        return a != b and a.lower() == b.lower()
