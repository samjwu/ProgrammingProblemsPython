class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stk = deque()
        
        n = len(s)
        
        chars = list(s)
        
        for i in range(n):
            c = chars[i]
            
            if c == "(":
                stk.append(i)
            elif c == ")":
                if len(stk) > 0:
                    stk.pop()
                else:
                    chars[i] = "_"
        
        while len(stk) > 0:
            idx = stk.pop()
            chars[idx] = "_"
            
        ans = ""
        
        for c in chars:
            if c == "_":
                continue
            
            ans += c
        
        return ans
