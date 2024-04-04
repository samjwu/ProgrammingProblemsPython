class Solution:
    def maxDepth(self, s: str) -> int:
        stk = deque()
        
        ans = 0
        
        for c in s:
            if c == "(":
                stk.append(c)
            elif c == ")":
                stk.pop()
            
            ans = max(ans, len(stk))
                
        return ans
